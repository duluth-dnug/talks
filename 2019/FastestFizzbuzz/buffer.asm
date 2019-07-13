%macro to_string 1
%push to_string_ctx
    %assign digit 1000000000
    %rep 10
        db  ('0' + (%1 / digit) % 10)
        %assign digit digit/10
    %endrep
%pop
%endmacro

%macro fizzbuzz 1
%push fizzbuzz_ctx
    %assign div_3 %1 % 3
    %assign div_5 %1 % 5
    %if div_3 == 0 && div_5 == 0
        db "Fizzbuzz!", 10
    %elif div_3 == 0
        db "Fizz", 10
    %elif div_5 == 0
        db "Buzz", 10
    %else
        to_string %1
        db 10
    %endif
%pop
%endmacro

buffer:
    %push bufferctx
    %assign i 1
    %rep 7680
        fizzbuzz i
        %assign i i+1
    %endrep
    %pop bufferctx
