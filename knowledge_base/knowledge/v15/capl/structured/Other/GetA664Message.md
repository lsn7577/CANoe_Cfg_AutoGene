# GetA664Message

> Category: `Other` | Type: `function`

## Syntax

```c
long GetA664Message (PDUobject aPDU, a664Message aMessage);
```

## Description

This function can be used within an “ON PDU”-handler to retrieve the A664Message object, to which the PDU corresponds.

The a664Message object then allows to retrieve the various runtime parameters like BAG or error flags via message selectors.

Note: the message ID is available, but not the message name.

## Parameters

| Name | Description |
|---|---|
| <aPDU> | The <this> object of the PDU-handler |
| <aMessage> | The a664Message object which getting the current message information |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | — | — | — | —✔ |
| Restricted To | AFDX | AFDX | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
