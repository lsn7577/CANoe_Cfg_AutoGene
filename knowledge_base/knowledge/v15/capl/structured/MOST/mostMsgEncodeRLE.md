# mostMsgEncodeRLE

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostMsgEncodeRLE(mostAmsMessage * msg, long fktIds[], long size);
```

## Description

mostMsgEncodeRLE() encodes a list of function IDs and saves it in the data area of a message. Run Length Encoding in accordance with MOST Specification 2.4 Para. 2.3.9 is used. This function is suitable for compiling messages of the FBlock.FktIds.Status type.

## Parameters

| Name | Description |
|---|---|
| msg | Message, which is to have data input into it. |
| fktIds[] | List of function IDs (can be unsorted). |
| size | Number of function IDs in fktIds[]. |

## Return Values

See error codes

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
