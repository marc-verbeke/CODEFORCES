import requests
url ="https://my.eos-contentia.be/MyContentiaBe_WD?FAQ=UNIGRO"
for i in range(0,1000000,1):
    pagina = requests.get(url)
