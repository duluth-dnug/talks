#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main() {
    size_t buffer_size = 256;
    char buf[buffer_size];
    char *b = buf;
    char num[buffer_size];
    int bytes_read;
    for(unsigned int i=1; i<=1000000000; ++i){
        bool fizz = (i % 3 == 0);
        bool buzz = (i % 5 == 0);
        bytes_read = getline(&b, &buffer_size, stdin);
        if(!(bytes_read > 0)){
            printf("Could not read line %u.\n", i);
            return 1;
        }
        else if(fizz && buzz){
            if(!strncmp(buf, "Fizzbuzz!", buffer_size)){
                printf("Bad input on line %u (should be \"Fizzbuzz!\"):\n", i);
                puts(buf);
                return 1;
            }
        }
        else if(fizz){
            if(!strncmp(buf, "Fizz", buffer_size)){
                printf("Bad input on line %u (should be \"Fizz\"):\n", i);
                puts(buf);
                return 1;
            }
        }
        else if(buzz){
            if(!strncmp(buf, "Buzz", buffer_size)){
                printf("Bad input on line %u (should be \"Buzz\"):\n", i);
                puts(buf);
                return 1;
            }
        }
        else{
            sprintf(num, "%010u", i);
            if(!strncmp(buf, num, buffer_size)){
                printf("Bad input on line %u (should be \"%010u\"):\n", i, i);
                puts(buf);
                return 1;
            }
        }
    }

    if(!(getline(&b, &buffer_size, stdin) < 0)){
        printf("Too many lines:");
        puts(buf);
        return 1;
    }
    else{
        puts("All tests pass!");
        return 0;
    }
}
