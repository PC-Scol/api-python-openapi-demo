# Utiliser le client openapi pour python

## Dépendances

- Installer python 3 : [Python](https://www.python.org/)

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

- On récupère la librairie java openapi

```bash
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.6.0/openapi-generator-cli-6.6.0.jar -O openapi-generator-cli.jar
```


- On génère le client openapi à partir de l'url du fichier de description de l'api openapi

```bash
java -jar openapi-generator-cli.jar generate -g python -c python-gen-config.json -i https://pegase-swagger-ui.dev.pc-scol.fr/fr.pcscol.ins.api/ins-gestion-api-v5/ins-gestion-api-v5-20.0.0.yaml -o generated/ins-gestion --package-name ins-gestion-client
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

