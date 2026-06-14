# RS232Receive

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232Receive( dword port, byte buffer[], dword size )
```

## Description

Receive blocks of bytes from a serial port.

## Return Values

0: error
The error occurs if
An error is only given if a problem is issued directly by the system.
To get informed about errors occurring in later stages of the operation use RS232OnError.

## Example

```c
byte mybuffer[20];
int mysize=20;
if ( 1==RS232Receive(1,mybuffer,mysize) )
  write(“It works with port 1.”);
...
RS232OnReceive( dword port, dword buffer[], dword number )
{
   // works after first RS232Receive !
   // buffer == mybuffer, 1<number<=mysize
}
```

## Availability

| Since Version |
|---|
