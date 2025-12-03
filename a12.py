# Student data
rno = 25
name = 'Hemant'
age = 21
per = 88.5
city = 'Pune'

#4 print () using format (most preferred method)
# a. empty place holder
print('Rno = {} Name = {} Age = {} Per = {} City = {}'.format(rno, name, age, per, city))

# b. index place holder
print('Name = {1} Rno = {0} Age = {2} Per = {3} City = {4}'.format(rno, name, age, per, city))

# c.  place holder accessing to data type :d for int, (:f) for float and (:s) for string
print('Rno = {:d} Name = {:s} Age = {:d} Per = {:.2f} City = {:s}'.format(rno, name, age, per, city))