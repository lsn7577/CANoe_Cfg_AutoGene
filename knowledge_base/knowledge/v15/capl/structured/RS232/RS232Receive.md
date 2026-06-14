# RS232Receive

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232Receive( dword port, byte buffer[], dword size );
```

## Description

Receive blocks of bytes from a serial port.

## Parameters

| Name | Description |
|---|---|
| port | A number between 1 and 255 identifying a serial port. |
| buffer | An array of bytes. |
| size | Maximum number of bytes which can be received. |

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
