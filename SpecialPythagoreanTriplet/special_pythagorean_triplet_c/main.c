#include <stdio.h>
#include <stdlib.h>


void pythagorean_triplet(int n)
{
    for (int i = 0; i < n/3; i++)
    {
        for (int j = 0; j < n/2; j++)
        {
            int k = n - i - j;
            if (i*i + j*j == k*k)
            {
                printf("%d , %d , %d",i,j,k);
                int product = i*j*k;
                printf("\n%d",product);
                return;
            }
        }

    }
    printf("No triplet found");
}

int main()
{
    int n = 1000;
    pythagorean_triplet(n);
    return 0;
}

