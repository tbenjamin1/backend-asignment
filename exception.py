

# from requests import exceptions
# from requests.models import HTTPError


# try:
#     file = open('test.txt')


# except FileNotFoundError as e:
#     print(e)
# except exceptions as e:
#     print(e)
# else:
#     print(file.read())
#     file.close
# finally:
#     print('now its working great...!!')

# http request


import requests
# resp = requests.get('https://reqres.in/api/users/h')
# try:
#     resp.raise_for_status()
# except requests.exceptions.HTTPError:
#     print("HTTP REQUEST ERROR")
# else:

#     print(resp)

# connection error

resp = requests.get('https://reqres.in/api/users')
try:
    resp.raise_for_status()
except requests.exceptions.ConnectionError:
    print("ConnectionError ERROR")
else:

    print(resp)
