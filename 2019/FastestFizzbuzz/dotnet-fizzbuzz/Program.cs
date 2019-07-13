using System;

namespace dotnet_fizzbuzz
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i = 1; i <= 1000000000; ++i){
                bool fizz = (i % 3 == 0);
                bool buzz = (i % 5 == 0);
                if(fizz && buzz){
                    Console.WriteLine("Fizzbuzz!");
                }
                else if(fizz){
                    Console.WriteLine("Fizz");
                }
                else if(buzz){
                    Console.WriteLine("Buzz");
                }
                else{
                    Console.WriteLine($"{i, 10:D10}");
                }
            }
            Console.WriteLine("Hello World!");
        }
    }
}
