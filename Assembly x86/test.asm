section .data			;section that declares data
	hello:     db 72,101,108,108,111,32,119,111,114,108,100,10    ; 'Hello world!\n'
	helloLen:  equ $-hello             ; Length of the 'Hello world!' string (I'll explain soon)


section .text			; section that contains code
	global _start

_start:
	mov eax,10			; for i = 5; i > 0; i--
	push eax			; store on stack

loop:

	mov eax,4			; The system call for write (sys_write)
	mov ebx,1			; File descriptor 1 - standard output
	mov ecx,hello		; Put the offset of hello in ecx
	mov edx,helloLen	; helloLen is a constant, so we don't need to say 
						;  mov edx,[helloLen] to get it's actual value
	int 0x80			; Call the kernel
	
	
	pop eax				; pop from stack

	cmp eax,0			; if greater than zero
	jne loop			; loop

	mov eax,1			; The system call for exit (sys_exit)
	mov ebx,0			; Exit with return code of 0 (no error)
	int 0x80

