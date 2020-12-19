#include <iostream>

using namespace std;

void pythagoreanTriplet(int n)
{
    for(int i = 0; i<n/3 ; i++)
    {
        for(int j = 0; j<n/2 ; j++)
        {
            int k = n-i-j;
            if(i*i + j*j == k*k)
            {
                cout <<i<<", "<<j<<", "<<k;
                int product = i*j*k;
                cout <<"\n"<<product;
                return;
            }

        }
    }
    cout <<"No triplet";
}
int main()
{
    int n = 1000;
    pythagoreanTriplet(n);
    return 0;
}
