hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
    g_p = h*r
else:
    ot_h= h-40
    ot_r= ot_h*1.5
    usual_pay=40*r
    ot_pay=ot_h*ot_r
    gross_pay=usual_pay+ot_pay
print("Gross pay is : "+ str(gross_pay))