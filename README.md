# Flask-KeyVault


A Flask extension to read and write secrets using [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/).

## Installation

```bash
$ pip install Flask-KeyVault
```
## Usage
```python
import os

from flask import Flask

from flask_keyvault import KeyVault
from flask_keyvault.exceptions import KeyVaultAuthenticationError

demo = Flask(__name__)

demo.config.update(
    AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID','YOUR-AZURE_CLIENT_ID'),
    AZURE_SECRET = os.getenv('AZURE_SECRET', 'YOUR-AZURE-SECRET'),
    AZURE_TENANT = os.getenv('AZURE_TENANT', 'YOUR-AZURE-TENANT')
)

keyvault = KeyVault()
keyvault.init_app(demo)

key_vault_url = 'https://mykeyvault.vault.azure.net/'

@demo.route('/')
def index():

    try:
        my_secret = keyvault.get(key_vault_url, "my_secret", 1)
        return my_secret
    except KeyVaultAuthenticationError:
        return "authentication error"

demo.run(debug=True)
```

## Contributing
Questions, comments or improvements, please create an issue on [Github](https://github.com/erikhoward/flask-keyvault/issues).

To suggest a change to the code or documentation, please create a new pull request on GitHub. Also, please squash multiple commits into a single commit in your pull request by rebasing onto the master branch.

## License
Flask-KeyVault is licensed under the [MIT](LICENSE) license.

## Contact
Erik Howard [@erik_howard](https://www.twitter.com/erik_howard).
