#include<stdio.h>

int fun();
int fun_return();
int fun_return_arg(int);

int main() {
	printf("Showing the Types of Functions and Use of it");
	
	fun();
	fun_return();
	fun_return_arg(4);
	

	}
	


	int fun()
	{

	printf("\n A lame Function with no Arguments/ parameters and No Return type.");

	}



	int fun_return()
	{
	int fees = 1000;
	printf("\n Return Type Function demoo");
	return fees;
	}
	

	int fun_return_arg(int n)
	{
	printf("Return Type and Takes Parameters too");
	if(n % 2 == 0){
	printf("The number is Even");
	}
	else{
	printf("The Number You have entered is ODD");
	}	

	}
