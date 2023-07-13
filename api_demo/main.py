#!/usr/bin/env python3

import os
import ins_gestion_client
from ins_gestion_client.rest import ApiException
from pprint import pprint

configuration = ins_gestion_client.Configuration(
    host = "https://ins-gestion.hotfix.pc-scol.fr/api/v5/ins",
    access_token = os.environ["BEARER_TOKEN"]
)

with ins_gestion_client.ApiClient(configuration) as api_client:
    api_instance = ins_gestion_client.ApprenantsApi(api_client)
    code_structure = 'ETAB00' # str | Le code de l'établissement
    code_apprenant = '20220117' # str | Le code Pegase de l'apprenant

    try:
        # Chercher les données d'un apprenant
        api_response = api_instance.lire_apprenant(code_structure, code_apprenant)
        print("The response of ApprenantsApi->lire_apprenant:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApprenantsApi->lire_apprenant: %s\n" % e)