using System;
using System.Numerics;

namespace SumOfDigitsof2_1000
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Sum of the digits of 2^1000");
            new Program().solution();
        }

        public void solution(){
            const int num = 2;
            const int expo = 1000;
            int result = 0;

            BigInteger number = BigInteger.Pow(num, expo);

            while(number > 0){
                result += (int)(number%10);
                number /= 10;
            }

            Console.WriteLine("The sum of digits {0}", result);
        }
    }
}
