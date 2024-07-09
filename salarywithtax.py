salary= 40000
tax_Rate= 0
if(salary<20000):
    tax_Rate= 15
elif(salary>=20000 and salary<50000):
    tax_Rate= 25
elif(salary>=50000 and salary<100000):
    tax_Rate= 30
else:
    tax_Rate= 35
Real_tax = (salary*tax_Rate)/100

print(f"Salary is: {salary}")
print(f"Tax rate is: {tax_Rate}")
print(f"Real Tax is: {Real_tax} ")

print(type(salary))
print(type(tax_Rate))
print(type(Real_tax))