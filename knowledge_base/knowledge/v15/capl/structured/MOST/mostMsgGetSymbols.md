# mostMsgGetSymbols

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostMsgGetSymbols(mostAmsMessage * msg, char[] fblock, char[] function, char[] optype, long bufferSize); // form 1
long mostMsgGetSymbols(mostMessage * msg, char[] fblock, char[] function, char[] optype, long bufferSize); // form 2
```

## Description

Determining the symbolic Names of the function block, the function and the Optype from an AMS or control message using the XML function catalog.

## Parameters

| Name | Description |
|---|---|
| msg | Message from which the symbolic names are determined. |
| fblock | Destination buffer for the function block name. |
| function | Destination buffer for the function name. |
| optype | Destination buffer for the optype name. |
| bufferSize | Destination buffer size. Valid for fblock, function and optype! |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
