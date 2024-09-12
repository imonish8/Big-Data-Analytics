#include<stdio.h>
// executes entire code instead of fun call.
inline int square_it(int n) 
{
	return n*n;
}

int main()
{
	int num;
	printf("Please enter a number below");
	scanf("%i",&num);
	int res = square_it(num);
	printf("The Square of the Entered Number is: %i",res);
}
