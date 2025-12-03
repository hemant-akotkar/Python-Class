#Bank Account
acno = 100
name = "Hemant"
bal = 12000

#1. Concatenation method
print("Account No = " + str(acno) + " Name = " + name + " Balance = " + str(bal))  

#2. Using Comma , as separator    
print("Account No =", acno, " Name =", name, " Balance =", bal)

3. f'string method
print(f"Account No = {acno} Name = {name} Balance = {bal}")'

#3. format () function method
print("Account No = {0} Name = {1} Balance = {2}".format(acno, name, bal))
print("Account No = {:d} Name = {:s} Balance = {:2f}".format(acno, name, bal))
