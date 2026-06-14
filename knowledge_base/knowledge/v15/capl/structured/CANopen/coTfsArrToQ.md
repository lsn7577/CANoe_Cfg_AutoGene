# coTfsArrToQ

> Category: `CANopen` | Type: `function`

## Syntax

```c
qword coTfsArrToQ( byte inByteArray[], dword arraysize );
```

## Description

The function converts the content of a byte array into a qword value.

## Parameters

| Name | Description |
|---|---|
| inByteArray[] | Array containing the bytes to be converted, recommended array size: 8 byte. |
| arraysize | Size of the array. |

## Return Values

Converted value or 0 if parameters are invalid.

## Example

```c
/* converts data from a byte array to a qword */
Byte inDataArr[8] = {8,7,6,5,4,3,2,1};
qword outValue;

outValue = coTfsArrToQ(inDataArr, 8);
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
