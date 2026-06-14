# mostApIsAddressed

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostApIsAddressed(long fblockID, long instID); // form 1
long mostApIsAddressed(mostAmsMessage * msgCommand); // form 2
```

## Description

mostApIsAddressed checks whether the functional MOST address {fblockID, instID} matches the CAPL node function blocks assigned via mostApRegister() or mostApRegisterEx(). The functional address is permitted to contain wildcard symbols.

This function can be used to determine whether an incoming command message is destined for the CAPL node.

## Parameters

| Name | Description |
|---|---|
| fblockID | Function block identifier of the functional address. |
| instID | Instance identifier of the functional address. |
| msgCommand | Received command message containing the functional address. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
