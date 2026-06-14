# SetRawSignal

> Category: `Test` | Type: `function`

## Syntax

```c
void SetRawSignal(char name[], int64 value); // form 3
long SetRawSignal(char name[], byte data[], dword dataLength); // form 4
```

## Description

Sets the raw value of a signal. These functions can be used for signals with more than 32 bits length. If the signal name is statically known, you can also use $<signal>.raw64 since 7.5 Service Pack 2.

## Parameters

| Name | Description |
|---|---|
| name | Name of the signal. Signal Ambiguity You have to use further objects to identify the signal uniquely. They are: channel, database name (alias), node name and message name. The exact qualification syntax is: [Channel::][Database name (alias)::][Node::][Message::]Signal The order and completeness of the objects from right to left is important (see example for getSignal) |
| value | Signal value to be set. |
| data | The data bytes of the signal. |
| dataLength | Length of the data. |

## Return Values

Form 4

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
