#!/usr/bin/python3
import numpy as np

p = float(input("Percentage of the population which have the disease [e.g. 3]: "))
TP = float(input("True positive rate in percent [e.g. 98]: "))
FP = float(input("False positive rate in percent [e.g. 4]: "))
FN = 100-TP; TN = 100-FP;
TP = TP/100; FP = FP/100; TN = TN/100; FN = FN/100;
i = 1

q = 100-p; p = p/100; q = q/100; 
T =  p*(TP+FN) + q*(FP+TN); 
#print("Total probability is %1.2f [should be 1.00]" %(T));
B = p*TP/(p*TP + q*FP);
print("-------------------------------------------------------------------------")
print("After %d test(s), probability of having the disease is %1.3f [%1.3f precent]" %(i, B,B*100))
print("-------------------------------------------------------------------------")

ans = str(input("Another test with the updated prior [y/n]? "))
while ans == 'y':
    i = i+1
    p = 100*B;
    q = 100-p; p = p/100; q = q/100; 
    T =  p*(TP+FN) + q*(FP+TN); 
    B = p*TP/(p*TP + q*FP);
    print("-------------------------------------------------------------------------")
    print("After %d test(s), probability of having the disease is %1.3f [%1.3f precent]" %(i, B,B*100))
    print("-------------------------------------------------------------------------")
    ans = str(input("Another test with the updated prior [y/n]? "))

    
        
