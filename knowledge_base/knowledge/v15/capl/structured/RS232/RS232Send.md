# RS232Send

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232Send( dword port, byte buffer[], dword number )
```

## Description

Sends a block of bytes to a serial port.

## Parameters

| Name | Description |
|---|---|
| port | A number between 1 and 255 identifying a serial port. |
| buffer | An array of bytes of which number will be sent. |
| number | Number of bytes to send. |

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
