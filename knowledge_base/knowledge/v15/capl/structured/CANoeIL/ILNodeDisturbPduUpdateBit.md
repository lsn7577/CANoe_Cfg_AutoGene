# ILNodeDisturbPduUpdateBit

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbPduUpdateBit(dbMsg aPDU, long disturbanceCount, long disturbanceValue);
long ILNodeDisturbPduUpdateBit(char aPDUName[], long disturbanceCount, long disturbanceValue);
```

## Description

This function modifies the update bit of a PDU. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Parameters

| Name | Description |
|---|---|
| aPDU | PDU, whose update bits will be disturbed. |
| aPDUName | Name of the PDU, whose update bits will be disturbed. Supported qualification patterns: [DBName::][NodeName::]aPDUName |
| -1 | Infinite. |
| 0 | Stops the disturbance, e.g.a infinite disturbance. |
| n | Number of disturbances. |
| updateBit | Desired disturbance value (0,1). |

## Example

```c
// Sets the PDU Update Bit 100 times to 0

variables {
  int disturbanceCount = 100;
  int updateBit = 0;
}

on key 'a'{
  ILNodeDisturbPduUpdateBit("PDU_A", disturbanceCount, updateBit);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP4 | 14 | 14 | — | — |
| Restricted To | — | FlexRay | FlexRay | FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
