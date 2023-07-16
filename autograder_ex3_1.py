hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
extra_hour=h-40
if extra_hour>0:
    # extra_hour=extra_hour
    gross_pay=(r*40)+(extra_hour*1.5)
else:
   gross_pay=r*h

print(gross_pay)

