bits 64

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

global _start
section .data

buffer:
    %push bufferctx
    %assign i 1
    %rep 7680
        fizzbuzz i
        %assign i i+1
    %endrep
    %pop bufferctx

section .text

increment_ascii_768:
    xor rax, rax
    add dword [rdi-3], ("0768" ^ "0000")
    mov rcx, 10

    cmp byte [rdi], '9'
    cmovg rax, rcx
    setg bl
    add byte [rdi-1], bl
    sub byte [rdi], al

    xor rax, rax
    cmp byte [rdi-1], '9'
    cmovg rax, rcx
    setg bl
    add byte [rdi-2], bl
    sub byte [rdi-1], al

    xor rax, rax
    cmp byte [rdi-2], '9'
    cmovg rax, rcx
    sub byte [rdi-2], al

    lea rdi, [rdi-3]
    test rax, rax
    jnz increment_ascii
    ret

carry:
    sub byte [rdi], 10
    dec rdi
increment_ascii:
    add byte [rdi], 1
    cmp byte [rdi], '9'
    jg carry
    ret

%macro increment_helper 1
    lea rdi, [r8 + %1]
    call increment_ascii_768
%endmacro

increment_buffer:
    push r8
    mov r8, buffer
.loop:
    increment_helper 0x08
    increment_helper 0x13
    increment_helper 0x23
    increment_helper 0x38
    increment_helper 0x43
    increment_helper 0x58
    increment_helper 0x68
    increment_helper 0x73
    add r8, 128
    cmp r8, buffer + 65536
    jne .loop
    pop r8
    ret

_start:
    mov r9, 130208
.loop:
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 65536
    syscall

    ;call increment_buffer

    sub r9, 1
    jne .loop

    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 21840
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall

