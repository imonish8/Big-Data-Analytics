#include<stdio.h>

int fibo(int n)
{
	if(n == 0)
		return 0;
	else if(n == 1)
		return 1;
	else
		return fibo(n-1)+fibo(n-2);
}

int main() 
{	
	int num;
	printf("\n Hello, This is Fibonacci Number Calculator:");
	printf("\n Please enter a number for which you want calculate Fibboncci Series");
	scanf("%i",&num);
	int result = fibo(num);
	printf("\n Fibonacci Series is: %d",result);


}
