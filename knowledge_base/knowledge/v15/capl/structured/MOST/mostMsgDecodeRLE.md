# mostMsgDecodeRLE

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostMsgDecodeRLE(mostAmsMessage * msg, long fktIds[], long buffersize);
```

## Description

mostMsgDecodeRLE() decodes the data area of a message and saves the function IDs in a list. Run Length Encoding in accordance with MOST Specification 2.4 Para. 2.3.9 is used. This function is suitable for evaluating messages of the FBlock.FktIds.Status type.

## Parameters

| Name | Description |
|---|---|
| msg | Message |
| fktIds[] | Destination buffer |
| buffersize | Size of the destination buffer |

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
