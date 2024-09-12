#include<stdio.h>


void isEvenOdd(int n)
{
	if(n % 2 == 0){
		printf("Entered Number is Even");
	}
	else{
		printf("Entered Number is Odd");
	}
}

int main() 
{
	int num = 0;
	printf("\n Enter a number here");
	scanf("%d",&num);
	isEvenOdd(num);
	
}

