bits 64
global _start

section .text
_start:
    mov rax, 1  ;write
    mov rdi, 1  ;stdout
    mov rsi, hello
    mov rdx, hello.len
    syscall

    mov rax, 60 ;exit
    xor rdi, rdi
    syscall

section .data

hello:
    db "Hello, world!", 10
.len: equ $-hello
