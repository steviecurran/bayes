#include <stdio.h> 
#include <math.h> 
#include <stdlib.h>
#include <string.h> 

int main()
{
int i;
float p, q, TP, FP, TN, FN, T, B;
char ans[2];

 printf("Percentage of the population which have the disease [e.g. 3]: "); scanf("%f", &p);
 printf("True positive rate in percent [e.g. 98]: "); scanf("%f", &TP);
 printf("False positive rate in percent [e.g. 4]: "); scanf("%f", &FP);
 
 i = 0;
 do{
    i= i+1;
     q = 100-p; FN = 100-TP; TN = 100-FP;
   p = p/100; q = q/100; TP = TP/100; FP = FP/100; TN = TN/100; FN = FN/100;

   T =  p*(TP+FN) + q*(FP+TN); 
   printf("\nTotal probability is %1.2f [should be 1.00]\n", T);

   B = p*TP/(p*TP + q*FP);
 
   printf("After %d test(s) Probability of having the disease is %1.3f [%1.3f precent]\n", i, B,B*100);

   printf("Another test with the updated prior [y/n]? "); scanf("%s", ans);

   p = 100*B; 

} while(strcmp(ans, "y") == 0);

}

// cc -o bayes bayes.c; ./bayes
