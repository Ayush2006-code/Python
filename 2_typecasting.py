name = "Ayush"
age = 20
gpa = 9.5
is_student = True
print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(gpa)) #<class 'float'>
print(type(is_student)) #<class 'bool'>

#now converting the data types
gpa =  int(gpa)
print(gpa)

age = str(age)
print(type(age))
age += "1"
print(age)