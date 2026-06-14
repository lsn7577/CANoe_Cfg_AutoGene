# getMessageName

> Category: `CAN` | Type: `function`

## Syntax

```c
dword getMessageName( dword id, dword context, char buffer[], dword size)
```

## Description

Finds out the message name.

## Parameters

| Name | Description |
|---|---|
| id | Id of the message for which the message name should be found. |
| CAN | 1 |
| LIN | 5 |
| MOST | 6 |
| FlexRay | 7 |
| J1708 | 9 |
| buffer | Buffer in which the message name is written. |
| size | Size of the buffer in Byte. |

## Return Values

If successful unequal 0, otherwise 0.

## Example

```c
variables
{
dword contextCAN = 0x00010000;
dword contextLIN = 0x00050000;
dword contextMOST = 0x00060000;
dword contextFLEXRAY = 0x00070000;
dword contextBEAN = 0x00080000;
dword contextJ1708 = 0x00090000;
}
on message *
{
char buffer[64];
if ( getMessageName( this.ID, contextCAN | this.CAN, buffer, elcount( buffer)))
{
write( "Message: %s", buffer);
}
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 4.0 | 4.0 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ (since version 7.1) | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (since version 7.1) | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (since version 7.1) | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (since version 7.1) | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ (since version 7.1) | ✔ | — | — | N/A |
