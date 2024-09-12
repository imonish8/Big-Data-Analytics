#include<stdio.h>

int main() 
{

	FILE *file = fopen("fib.c","r");
	
	if(file == NULL){
	printf("ERROR OPENING FILE \n");
	return 1;
	
	
	}
	char buffer[256];
	while(fgets(buffer,sizeof(buffer),file)){
	printf("%s",buffer);

	}

	fclose(file);
	
	return 0;
}
