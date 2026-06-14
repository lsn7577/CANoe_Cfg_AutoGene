# mostParamGetString

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamGetString (mostAmsMessage msg, char paramAdr[], char buffer[], long buffersize); // form 1
long mostParamGetString (mostAmsMessage msg, char paramAdr[], long arrayIndex, char buffer[], long buffersize); // form 2
```

## Description

Query of parameters of the String type from an AMS message using the parameter name from the XML function catalog.

## Parameters

| Name | Description |
|---|---|
| msg | Message from which the parameter should be read. |
| paramAdr | Identification of parameters (see Symbolic Identification of Parameters). |
| arrayIndex | Parameter index in arrays or sequences. This declaration overwrites the indexing in the brackets of <paramAdr>. |
| buffer | Buffer to which the parameter bytes are copied. |
| buffersize | Maximum number of copied parameter bytes (can be specified with (elcount(buffer))). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
