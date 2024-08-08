#include<stdio.h>
int main()
{
    int r,v,a,h,r2;
    printf("Enter the radius of the circle : ");
    scanf("%d",&r);
    float pie=3.14;
    a=pie*r*r;
    printf("The Area of the circle is : %d", a);
    printf("\nEnter the height of the cylinder : ");
    scanf("%d",&h);
    printf("Enter the radius of the cylinder : ");
    scanf("%d",&r2);
    v=pie*r2*r2*h;
    printf("The volume of the cylinder is : %d", v);
    
    
}
