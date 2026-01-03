# requests para requisições HTTP
import requests  # type: ignore

# http:// -> porta 80
# https:// -> porta 443

url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)  # formato de bytes (b)
print(response.text)

# print(response.json()) 
# # pode ser usando no caso de APIs que respondem em json