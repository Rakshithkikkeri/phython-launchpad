data_student={}
number=int(input("enter the number of students: " ))
i=1
while i<=number:
	usn=input("enter the usn value: ")
	name=input("enter your name: ")
	i=i+1

	data_student[usn]=name

print(data_student)

