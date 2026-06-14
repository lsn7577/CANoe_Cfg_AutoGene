# coTfsArrToW

> Category: `CANopen` | Type: `function`

## Syntax

```c
word coTfsArrToW( byte inByteArray[], dword arraysize );
```

## Description

The function converts the content of a byte array into a word value.

## Parameters

| Name | Description |
|---|---|
| inByteArray[] | Array containing the bytes to be converted, recommended array size: 2 byte. |
| arraysize | Size of the array. |

## Return Values

Converted value or 0 if parameters are invalid.

## Example

```c
/* converts a data from a byte array to a word */
Byte inDataArr[2] = {2,1};
Word outValue;

outValue = coTfsArrToW(inDataArr, 2);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
