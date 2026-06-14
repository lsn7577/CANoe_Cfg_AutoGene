# mostParamSetData

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamSetData(mostAmsMessage msg, char paramadr[], byte data[], long datalen); // form 1
long mostParamSetData(mostAmsMessage msg, char paramadr[], long arrayIndex, byte data[], long datalen); // form 2
```

## Description

Setting of parameters of the String type or RawStream in an AMS message using the parameter name from the XML function catalog.

When writing a string parameter with mostParamSetData 'data' has to include the coding byte and terminator character (mostParamSetString can be used for ASCII coding).

## Parameters

| Name | Description |
|---|---|
| msg | Message in which the parameter bytes should be written. |
| paramAdr | Identification of parameters (see Symbolic Identification of Parameters). |
| arrayIndex | Parameter index in arrays or sequences. This declaration overwrites the indexing in the brackets of <paramAdr>. |
| data | Data from which the parameter bytes are copied. |
| datalen | Number of valid parameter bytes that are copied to the message. |

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
