#include<stdio.h>
	// two methods call by ref, value
	
	void modifyValue(int sum)
	//void modifyRef(int *sum)
	{
	//*sum = 20;
	sum = 20;
	printf("The Value inside the ModifyValue is: %i",sum);
	}
	
	
int main()
{

	int sum = 10;
	printf("Call by Value before Calling the Function: %i",sum);
	modifyValue(&sum);
	//modifyRef(sum);
	printf("Call by Value demo after Calling the Fun. %i",sum);



}


