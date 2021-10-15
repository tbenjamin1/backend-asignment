

from requests import exceptions


try:
    file = open('test.txt')


except FileNotFoundError as e:
    print(e)
except exceptions as e:
    print(e)
else:
    print(file.read())
    file.close
finally:
    print('now its working great...!!')
