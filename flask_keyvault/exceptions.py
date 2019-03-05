# -*- coding: utf-8 -*-


class KeyVaultBaseException(Exception):
    """
    Base exception in which all flask_azurekeyvault errors extend
    """
    pass


class KeyVaultAuthenticationError(KeyVaultBaseException):
    """
    An error with authentication

    Attributes:
        message: explanation of the error
    """
    pass
