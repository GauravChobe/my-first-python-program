# the solution of the quadratic equation
print "please enter the values for a,b,c in a*x**2+b*x+c "
a= float(raw_input())
b= float(raw_input())
c= float(raw_input())
if (b**2 - 4*a*c) > 0 :
    print "one root of the equation is", ( -b + (b**2-4*a*c)**0.5 ) / 2*a
    print "other root of the equation is", ( -b - (b**2-4*a*c)**0.5 ) / 2*a
else :
    print "the roots are imaginary"
