#!/usr/bin/env python3
from __future__ import print_function

import os
from pprint import pprint

import swagger_client  # type: ignore
from swagger_client.rest import ApiException  # type: ignore

# Configuration de l'url et de l'authentification
configuration = swagger_client.Configuration()
configuration.host = "https://ins.hotfix.pc-scol.fr/api/v5/ins"
configuration.api_key_prefix["Authorization"] = "Bearer"
configuration.api_key["Authorization"] = os.environ["BEARER_TOKEN"]


# Monkey patch auth_settings (bug: https://github.com/swagger-api/swagger-codegen/issues/10060)
def auth_settings(self):
    return {
        "idTokenAuth": {
            "type": "http",
            "in": "header",
            "key": "Authorization",
            "value": self.get_api_key_with_prefix("Authorization"),
        },
    }


swagger_client.Configuration.auth_settings = auth_settings

# Création de l'instance de l'API
api_instance = swagger_client.ApprenantsApi(swagger_client.ApiClient(configuration))
code_structure = "ETAB00"  # str | Le code de l'établissement
code_apprenant = "20220117"  # str | Le code Pegase de l'apprenant

try:
    # Chercher les données d'un apprenant
    api_response = api_instance.lire_apprenant(code_structure, code_apprenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprenantsApi->lire_apprenant: %s\n" % e)
