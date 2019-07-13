#include <stdio.h>

int main(){
    char* message =
        "%010u\n"
        "%010u\n"
        "Fizz\n"
        "%010u\n"
        "Buzz\n"
        "Fizz\n"
        "%010u\n"
        "%010u\n"
        "Fizz\n"
        "Buzz\n"
        "%010u\n"
        "Fizz\n"
        "%010u\n"
        "%010u\n"
        "Fizzbuzz\n";
    for(unsigned int i=1;i<=1000000000; i+=15){
        printf(message, i, i+1, i+3, i+6, i+7, i+10, i+12, i+13);
    }
}
