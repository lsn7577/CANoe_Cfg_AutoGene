# mostAsNtfOutput

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfOutput(long destAdr, mostMessage msg); // form 1
long mostAsNtfOutput(long destAdr, mostAmsMessage msg); // form 2
```

## Description

destAdr != 0xFFFF:

The command sends the message to the stated address.

destAdr == 0xFFFF:

The message is sent to the address of all notification clients. The FBlockID, InstID and FunctionID values, which are needed to read the addresses from the notification matrix, are extracted from the message variable (msg).

## Parameters

| Name | Description |
|---|---|
| destAdr | Message destination address or 0xFFFF to send to all notification clients. |
| msg | Message to be sent. |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
