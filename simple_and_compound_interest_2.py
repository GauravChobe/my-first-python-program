# To calculate the simple and compound interest
print "please enter the priciple amount"
p=float(raw_input())
print "please enter the number of years"
n=float(raw_input())
print "please enter the rate of interst"
i=float(raw_input())
simple_interest=(p*i*n)/100
compound_interest=p*((1+i/100)**n)
print "the simple interest is", simple_interest
print "the compound interest is", compound_interest
