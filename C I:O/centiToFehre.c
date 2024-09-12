#include<stdio.h>
int main()
{
  float cent, fahr;
  scanf("%f", &cent);
  fahr = cent*(9.0/5.0) + 32;
  printf("%f C Equals %f \n" , cent , fahr);
  return 0;
}
