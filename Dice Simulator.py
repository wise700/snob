from random import randint

def generate():
    return randint(1,6)

input('Hi press enter to roll the dice!!!')
print(generate())
response=input("Do you want to roll dice again??")

while response =="yes":
    print(generate())
    response = input("Do you want to roll dice again??")





