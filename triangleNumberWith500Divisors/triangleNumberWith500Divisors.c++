#include <iostream>
#include <math.h>

using namespace std;

int numOfDiv(int num);

int main()
{
    unsigned long long triangleNum = 1;
    unsigned long long currentNum = 2;
    int target = 500;
    int numOfDivisors  = 0;

    numOfDivisors = numOfDiv(triangleNum);
    while(numOfDivisors<target){
        triangleNum+=currentNum;
        currentNum++;
        numOfDivisors = numOfDiv(triangleNum);
    }

    cout<<"\nTriangle Number = "<<triangleNum;

    return 0;
}
/**
    Function to check the number of divisors
    Function's working fine
 */

int numOfDiv(int num)
{
    int divNum = 0;
    if(num==1){
        divNum = 1;
    }
    else
    {
        int numSqrt = (int)sqrt(num);
        for(int i = 1;i<=numSqrt;i++)
        {
            if(num%i==0)
            {
                divNum += 2;
            }
        }
        if(numSqrt*numSqrt == num)
        {
            divNum += 1;
        }
    }
    cout<<"\nNumber of Divisors = "<<divNum;
    return divNum;
}
