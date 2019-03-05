# -*- coding: utf-8 -*-
"""
    Flask-KeyVault
    :author: Erik Howard <erikhoward@protonmail.com>
    :license: MIT
    -------------------

    Allows reading of Azure Key Vault secrets for Flask applications.
"""
import os
from logging import getLogger

from azure.keyvault import KeyVaultClient, KeyVaultAuthentication, KeyVaultId
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_active_directory import MSIAuthentication
from msrest.exceptions import AuthenticationError

from .exceptions import KeyVaultAuthenticationError
from .version import __version__

log = getLogger(__name__)


class KeyVault(object):
    """
    The Azure Key Vault flask extension is responsible for getting and
    setting Azure Key Vault secrets.
    """

    AUTH_RESOURCE = "https://vault.azure.net"

    def __init__(self, app=None, client_id=None, secret=None, tenant=None):
        """
        Initialize the flask extension

        :param app: flask.Flask application instance
        :param client_id: the Azure app registration (client) id
        :param secret: the app registration secret
        :param tenant: the Azure tenant that the app (client) belongs too
        """

        self.client_id = client_id
        self.secret = secret
        self.tenant = tenant
        self._credentials = None
        self._client = None
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Init the Flask_AzureKeyVault extension"""
        if self.client_id is None:
            self.client_id = app.config.get("AZURE_CLIENT_ID", '')
        if self.secret is None:
            self.secret = app.config.get("AZURE_SECRET", '')
        if self.tenant is None:
            self.tenant = app.config.get("AZURE_TENANT", '')

    @property
    def client(self):
        """
        Get an instance of the key vault client
        """

        if self._client is None:
            self._client = KeyVaultClient(self.credentials)

        return self._client

    @property
    def credentials(self):
        """
        Construct key vault credentials
        """
        if self._credentials is None:
            self._credentials = self._get_credentials()
        return self._credentials

    def _get_credentials(self):
        """
        Try to get a token via MSI, or fallback to service principal auth
        """

        credentials = None
        if "APPSETTING_WEBSITE_SITE_NAME" in os.environ:
            credentials = MSIAuthentication(
                resource=self.AUTH_RESOURCE
            )
        else:
            try:
                credentials = ServicePrincipalCredentials(
                    client_id=self.client_id,
                    secret=self.secret,
                    tenant=self.tenant,
                    resource=self.AUTH_RESOURCE
                )
            except AuthenticationError:
                raise KeyVaultAuthenticationError('Error authenticating')

        return credentials

    def get(self, vault_url, secret_name):
        result_bundle = self.client.get_secret(
            vault_url, secret_name, KeyVaultId.version_none)
        return result_bundle.value

    def set(self, vault_url, secret_name, secret_value):
        self.client.set_secret(vault_url, secret_name, secret_value)
