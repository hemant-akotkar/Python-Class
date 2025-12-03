# input () data from keyboard

rno = input('Enter roll number: ')
name = input('Enter name: ')
per = input('Enter percentage: ')

print(f'Roll No = {rno} Name = {name} Percentage = {per}')
print(type(rno), type(name), type(per) )

#every data entered using input () is string type
rno = input('Enter roll number: ')
name = input('Enter name: ')
per = float(input('Enter percentage: '))
print(type(rno), type(name), type(per) )
