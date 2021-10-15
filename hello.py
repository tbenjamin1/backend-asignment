# class Employee:
#     def __init__(self,first,last,age,email):
#       self.first =first
#       self.last =last
#       self.age =age
#       self.email =f'{self.first}.{self.last}'

#     @property
#     def fullname(self):
#     return f'{self.first}.{self.last}'

#     class Developer(Employee):
#         def __init__(self, first, last, age, email, prog_lang):
#           super().__init__(first,last,age)


#            self.prog_lang = prog_lang

#            dev_1 = Developer('jhon','doe',45,'java')
#            print(dev_1.prog_lang)
#            print(dev_1.first)
#            print(dev_1.age)
#            print(dev_1.last)


# abstract class

# from abc import ABC
# class Animal()

# # class Human(Animal):
#     def move(self):
#       print('icant move')
# class Dog(Animal):
#     def move(self):
#       print('icant move')
#       hum= Hum()
#       hum.move()
#       dg = dog()

# import requests

# get method
# url = 'http://api.open-notify.org/astros.json'

# response = requests.get(url)

# print(response.json())

# query = {'lat':'45','lon':'180'}
# url_1 ='http://api.open-notify.org/iss-pass.json'
# response_1 = requests.get(url_1,params=query)
# print(response_1.json)

# import json

# import requests

# url = "https://reqres.in/api/users"

# payload =json.dumps({
#     "name":"ben",
#     "job":"dev"
# })

# headers ={
#     "content-Type":"application/json"
# }
# Response = requests.post(url,headers=headers,data=payload)

# print(Response.json())


# assert i n python


def avg(marks):
    assert len(marks) != 0, "list is empty."
    return sum(marks)/len(marks)


# marks2 = [2, 4, 8, 9]
# print(avg(marks2))

marks1 = []

print(avg(marks1))
