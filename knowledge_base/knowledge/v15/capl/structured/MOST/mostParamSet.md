# mostParamSet

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamSet(mostAmsMessage msg, char paramAdr[], double value); // form 1
long mostParamSet(mostAmsMessage msg, char paramAdr[], long arrayIndex, double value); // form 2
```

## Description

Setting of a parameter value in an AMS message using the parameter name from the XML function catalog.

Suitable for parameter types 'Number', 'Enum', 'BitField' and 'Bool'.

For parameters of the 'Enum' type, the numeric value can be specified. The mostParamSetString function can be used to set the symbolic value.

## Parameters

| Name | Description |
|---|---|
| msg | Message in which the parameter value should be described. |
| paramAdr | Identification of parameters (see Symbolic Identification of Parameters). |
| arrayIndex | Parameter index in arrays or sequences. This declaration overwrites the indexing in the brackets of <paramAdr>. |
| value | Value of the parameter with whole-number parameter types, decimal places are truncated. A raw value is expected i. e. no conversion formula is applied. |

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
