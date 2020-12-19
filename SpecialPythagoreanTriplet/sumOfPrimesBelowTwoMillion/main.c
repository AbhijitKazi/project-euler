#include <stdio.h>
int main()
{
 int count;
 int n = 20;
 long i,a,sum=0;
 printf("Prime numbers between 100 and 500 are : \n");
 for (i=0;i<=n;i++)
 {
	 count=0;
		 for (a=1;a<=n;a++)
		 {
 			if (i%a==0)
 				count++;
 		 }
	 if (count==2)
        sum=sum+i;

 }
 printf("%ld\t",sum);
 return 0;
}
