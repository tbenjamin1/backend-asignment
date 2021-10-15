
# import json
# import requests


# url = "https://reqres.in/api/users/auth/api-key"

# payload = json.dumps({
#     "name": "ben",
#     "job": "dev"
# })

# headers = {

#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }

# Response = requests.post(url, headers=headers, data=payload)

# print(Response.json())

# token = Response.get("access_token")
# refresh = Response.get("refresher_token")

# # when token expires use refresher token

# url = "https://reqres.in/api/users/auth/refresh"

# payload = json.dumps({
#     {" refresherTokens": refresh}
# })

# headers = {

#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }

# Response = requests.post(url, headers=headers, data=payload)

# print(Response.json())


import requests
from requests.auth import HTTPBasicAuth
from requests.sessions import session

auth_token = ""
user_name = "benjamin"
BASE_URL = "http://localhost:8080"

session = requests.session()

resp = session.get(BASE_URL +,
                   auth=HTTPBasicAuth(user_name, auth_token))

print(resp.json())
