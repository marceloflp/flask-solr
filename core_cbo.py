import requests

SOLR_URL = "http://localhost:8983/solr"
CORE_NAME = "cbo"
CONFIGSET = "_default" 

response = requests.get(
    f"{SOLR_URL}/admin/cores",
    params={
        "action": "CREATE",
        "name": CORE_NAME,
        "configSet": CONFIGSET,
        "instanceDir": f"/var/solr/data/{CORE_NAME}"
    }
)

if response.status_code == 200:
    print("Core criado com sucesso!")
else:
    print("Erro:", response.json())