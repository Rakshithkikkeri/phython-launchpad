name=input('Enter your name:')
age=int(input('enter your age:'))
import datetime
cureent_year=datetime.datetime.today().year
Birth_year=cureent_year-age
Hundreth_year=Birth_year+100

print(f"Hey {name} ! you'll turn 100 years old in {Hundreth_year}")