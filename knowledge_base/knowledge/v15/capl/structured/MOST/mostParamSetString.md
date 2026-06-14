# mostParamSetString

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamSetString (mostAmsMessage msg, char paramAdr[], char value[]); // form 1
long mostParamSetString (mostAmsMessage msg, char paramAdr[], long arrayIndex, char value[]); // form 2
```

## Description

Setting of parameters of the String type (for ASCII-coded strings only) or of the 'Enum' type in an AMS message using the parameter name from the XML function catalog.

## Parameters

| Name | Description |
|---|---|
| msg | Message in which the parameter value should be described. |
| paramAdr | Identification of parameters (see Symbolic Identification of Parameters). |
| arrayIndex | Parameter index in arrays or sequences. This declaration overwrites the indexing in the brackets of <paramAdr>. |
| value | String: Characters that should be copied to the message.Enumeration: Symbolic name of the parameter value. |

## Return Values

See error codes

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
