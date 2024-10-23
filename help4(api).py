import json, requests

response = requests.get("http://jsonplaceholder.typicode.com/comments")
statusCode = response.status_code

if statusCode > 202:
    print("Ocorreu um erro ao tentar acessar o seu request")
else:
    print("Conectado com sucesso !!!")
    comments = json.loads(response.content)

    for comment in comments:
        print comment
pip install requests
