#include<stdio.h>
int main()
{
    float s,p,r,t;
    printf("Enter the principal amount : ");
    scanf("%f",&p);
    printf("Enter the interest rate per annum : ");
    scanf("%f",&r);
    printf("Enter the time in years : ");
    scanf("%f",&t);
    s= (p*r*t)/100;
    printf("Simple interst is : %f",s);
}
