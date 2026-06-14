# RS232Send

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232Send( dword port, byte buffer[], dword number )
```

## Description

Sends a block of bytes to a serial port.

## Return Values

0: error
The error occurs if
An error is only given if a problem is issued directly.
To get informed about errors occurring in later stages of the operation use RS232OnError.

## Example

```c
char text[20] = “Hello World !”;
byte buffer[20];
int i;
int length;
length=strlen(text)+1;
for (i=0;i<length;i++) buffer[i]=text[i];
if ( 1==RS232Send(1,buffer,length) )
   write(“It works with port 1.”);
```

## Availability

| Since Version |
|---|
