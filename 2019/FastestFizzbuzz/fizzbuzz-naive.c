#include <stdio.h>
#include <stdbool.h>

int main(){
    for(unsigned int i=1; i <= 1000000000; ++i){
        bool fizz = (i%3==0);
        bool buzz = (i%5==0);
        if(fizz && buzz){
            puts("Fizzbuzz!");
        }
        else if(fizz){
            puts("Fizz");
        }
        else if(buzz){
            puts("Buzz");
        }
        else{
            printf("%010u\n", i);
        }
    }
}
