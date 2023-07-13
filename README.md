# Utiliser le client openapi pour python

Exemple d'utilisation du client openapi pour python


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

- On récupère la librairie java openapi. A l'écriture de cette doc, on utilise la version 6.6.0 avec le client python-nextgen

```bash
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.6.0/openapi-generator-cli-6.6.0.jar -O openapi-generator-cli.jar
```

- On ajoute un fichier de conf pour openapi appelé **python-gen-config.json**

```js
{
  "pythonAttrNoneIfUnset": true
}
```


- On génère le client openapi à partir de l'url du fichier de description de l'api openapi

```bash
java -jar openapi-generator-cli.jar generate -g python-nextgen -c python-gen-config.json -i https://pegase-swagger-ui.hotfix.pc-scol.fr/fr.pcscol.ins.api/ins-gestion-api-v5/ins-gestion-api-v5-20.0.0.yaml -o generated/ins-gestion --package-name ins_gestion_client
```

- On ajoute le client généré à notre projet :

```bash
poetry add generated/ins-gestion/
```

- On ajoute le token d'authentification généré au tout debut dans une variable d'env

```bash
export BEARER_TOKEN=S3CR3T
```

- On crée un script **api_demo/main.py**, on lui donne les droits d'exécution et on teste


```bash
touch api_demo/main.py
```

```python
#!/usr/bin/env python3

if __name__ == "__main__":
    print("Hello")
```

```bash
chmod +x api_demo/main.py
poetry run api_demo/main.py
```

