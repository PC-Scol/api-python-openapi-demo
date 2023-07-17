# Utiliser le client openapi pour python

Exemple d'utilisation du client openapi pour python.\
On utilise swagger-codegen plutôt que openapi-generator car, pour le moment, celui-ci génére du code avec des erreurs. 


## Prise en main APIs Swagger :

- Visiter https://pegase-swagger-ui.hotfix.pc-scol.fr
- Récupération token via curl : 

```bash
curl -d "username=svc-api&password=???&token=true" \
-H "Content-Type: application/x-www-form-urlencoded" \
-X POST https://authn-app.hotfix.pc-scol.fr/cas/v1/tickets
```

- Appel du endpoint "lecture d'un établissement par code pegase"
- (Optionnel) Appel du endpoint "création d'un nouvel établissement"
- (Optionnel) Exploration des autres APIs


## Dépendances

- Installer python >= 3.11 : [Python](https://www.python.org/)

```bash
apt install python3
```

- Installer poetry pour la gestion des dépendances et du packaging : [Poetry](https://python-poetry.org/)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## Préparation du projet

- On crée un projet python avec poetry

```bash
poetry new api-demo
cd api-demo
```

- On récupère la librairie java swagger-codegen. A l'écriture de cette doc, on utilise la version 3.0.43 avec le client python

```bash
wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.43/swagger-codegen-cli-3.0.43.jar -O swagger-codegen-cli.jar
```

- On génère le client à partir de l'url du fichier de description de l'api

```bash
java -jar swagger-codegen-cli.jar generate -i https://pegase-swagger-ui.hotfix.pc-scol.fr/fr.pcscol.ins.api/ins-gestion-api-v5/ins-gestion-api-v5-20.0.0.yaml -l python -o generated/ins-gestion/

```

- On ajoute le client généré à notre projet :

```bash
poetry add generated/ins-gestion/
```

- On ajoute le token d'authentification généré au tout debut dans une variable d'env

```bash
export BEARER_TOKEN=S3CR3T
```

- On crée un script **api_demo/main.py**, on lui donne les droits d'exécution :


```bash
touch api_demo/main.py
chmod +x api_demo/main.py
```

- Dans **api_demo/main.py**, on écrit le code pour lire un apprenant :

```python
#!/usr/bin/env python3
from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import os

# Configuration de l'url et de l'authentification
configuration = swagger_client.Configuration()
configuration.host = "https://ins.hotfix.pc-scol.fr/api/v5/ins"
configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration.api_key['Authorization'] = os.environ['BEARER_TOKEN']

# Monkey patch auth_settings (bug: https://github.com/swagger-api/swagger-codegen/issues/10060)
def auth_settings(self):
        return {
            'idTokenAuth':
                {
                    'type': 'http',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': self.get_api_key_with_prefix('Authorization')
                },
        }^
swagger_client.Configuration.auth_settings = auth_settings

# Création de l'instance de l'API
api_instance = swagger_client.ApprenantsApi(swagger_client.ApiClient(configuration))
code_structure = 'ETAB00' # str | Le code de l'établissement
code_apprenant = '20220117' # str | Le code Pegase de l'apprenant

try:
    # Chercher les données d'un apprenant
    api_response = api_instance.lire_apprenant(code_structure, code_apprenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprenantsApi->lire_apprenant: %s\n" % e)

```

- On exécute le script via :

```bash
poetry run api api_demo/main.py
```

- Vous devriez alors voir apparaître dans la console les informations de l'apprenant si tout c'est bien passé.