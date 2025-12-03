# Student data
rno = 25
name = 'Hemant'
age = 21
per = 88.5
city = 'Pune'

print('\nRno ={:20d} \nName ={:>20s} \nAge ={:<20d} \nPer ={:20.2f} \nCity ={:20s}'.
     format(rno, name, age, per, city))

print('\nRno ={:#>20d} \nName ={:*>20s} \nAge ={:*>20d} \nPer ={:*>20.2f} \nCity ={:*>20s}'.
     format(rno, name, age, per, city))

print('\nRno ={:<20d} \nName ={:<20s} \nAge ={:<20d} \nPer ={:<20.2f} \nCity ={:<20s}'.
     format(rno, name, age, per, city))