#include <stdio.h>

int main(){
    char buf[10];
    char* arr[] = {
        buf,
        "Fizz",
        "Buzz",
        "Fizzbuzz"
    };
    for(unsigned int i=1; i<=1000000000; i++){
        sprintf(buf, "%010u", i);
        puts(arr[(!(i%5)<<1)|(!(i%3))]);
    }
}
