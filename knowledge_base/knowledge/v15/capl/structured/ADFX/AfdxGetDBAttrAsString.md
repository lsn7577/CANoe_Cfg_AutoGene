# AfdxGetDBAttrAsString

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetDBAttrAsString( long msgID, char attrName[], long bufSize, char buffer[]);
```

## Description

Retrieves a message attribute value in string representation from a given message ID.

## Parameters

| Name | Description |
|---|---|
| msgID | Unique message ID as defined in the DBC. |
| attrName | Name of the message attribute. |
| bufSize | Size of the provided buffer to get the value into. |
| buffer | Buffer which should hold the found value. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
