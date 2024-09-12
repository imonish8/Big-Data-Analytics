#include<stdio.h>

int sq_area(int len)
{
	return len*len;
}

int rec_area(int len, int wide)
{
	return 2*len*wide;
}

int main() 
{
	int result_sq = sq_area(33);
	int result_rec = rec_area(22,33);
	printf("The Square Area of Infrastructure is: %i",result_sq);
	printf("The rectangular Area is : %i",result_rec);

}
