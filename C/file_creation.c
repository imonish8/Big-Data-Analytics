#include<stdio.h>

int main()  
{
	FILE *file;

	file  = fopen( "prepro_file.c", "w");
		
	if( file == NULL){\
		printf("ERROR OPENING THE prepro_file.c");
		return 1;
	}	
	
	fprintf(file, "#include<stdio.h>\n \n");

	fclose(file);
	
	printf("File has been successfully Created \n And I have named it as prepro C File, Opened and CLosed Completely");
}
