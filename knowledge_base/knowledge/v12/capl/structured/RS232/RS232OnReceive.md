# RS232OnReceive

> Category: `RS232` | Type: `function`

## Syntax

```c
RS232OnReceive( dword port, byte buffer[], dword number )
```

## Description

Callback handler for reception of data at a serial port.

Will be called only at the nodes which issued a RS232Receive operation for the given port.

The handler will only be called for success. For errors RS232OnError will be called.

The buffer may be much larger than number. For very slow connections, the handler may get called for few bytes. At least one byte is given.

It is possible to listen to one and the same port at several nodes. All nodes will be called with the same data.

## Return Values

0: error
The error occurs if no start receive operation has been.

## Example

```c
// at sender node
char text[20] = “Hello World !”;
byte block[20];
int i;
int length;
length=strlen(text)+1;
for (i=0;i<length;i++) block[i]=text[i];

if ( 0!=RS232Send(1,block,length) )
   write(“Written block of bytes to port 1.”);
...
// at receiver node (here 2)
byte mybuffer[100];
int mysize = 100;
RS232Receive(2,mybuffer,mysize);
...
// at node which issued the receive request
RS232OnReceive(dword port, byte buffer[], dword number)
{
   // port==2 here
   // buffer==mybuffer, number<=mysize
   // buffer contains some parts of block
}
```

## Availability

| Since Version |
|---|
