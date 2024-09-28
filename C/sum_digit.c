#include<stdio.h>

int main ()
{
	int num, sum = 0;
	printf("Please Enter a Number to calculate the sum of digits");
	
	scanf("%d",&num);
	for(;num != 0; num/= 10)
	{
	
	sum += num % 10;
	}
	printf("\n Sum of Digits is: %d",sum);

} 
