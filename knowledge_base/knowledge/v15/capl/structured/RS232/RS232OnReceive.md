# RS232OnReceive

> Category: `RS232` | Type: `function`

## Syntax

```c
RS232OnReceive( dword port, byte buffer[], dword number );
```

## Description

Callback handler for reception of data at a serial port.

## Parameters

| Name | Description |
|---|---|
| port | A number between 1 and 255 identifying a serial port. |
| buffer | The buffer given to the start receive call. |
| Note The number of received bytes will vary strongly with the speed of the connection. |  |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 | 7.1 | — | — | 14 | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | — | — | ✔ | N/A |
