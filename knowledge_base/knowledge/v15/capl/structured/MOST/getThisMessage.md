# getThisMessage

> Category: `MOST` | Type: `function`

## Syntax

```c
GetThisMessage(mostAMSMessage msg, long count);
```

## Description

Copies the data of a AMS message into the msg variable.

This function must be used exclusively within a an event procedure on mostAMSMessage.

## Parameters

| Name | Description |
|---|---|
| msg | Variable of the type mostAmsMessage. |
| count | Number of use data bytes that have to be copied. |

## Return Values

—

## Example

The following program section copies 1000 bytes of a message's useful data to the local variable msg on Channel 1. Afterwards the contents of byte 500 are output to the Write Window.

```c
on mostAMSMessage MsgChannel1.*
{
   mostAMSMessage * msg = { DLC = 1000 };
   GetThisMessage(msg, 1000);
   write(“Byte 500: %02X”, msg.byte(500));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.1 | 3.1 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
