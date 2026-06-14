# coTfsWToArr

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsWToArr( word wordValue, byte outByteArray[], dword arraysize );
```

## Description

The function converts a word value into a byte array.

## Parameters

| Name | Description |
|---|---|
| wordValue | Value to be converted. |
| outByteArray[] | Array containing the converted value, recommended array size: 2 byte. |
| arraysize | Size of the byte array. |

## Return Values

Error code

## Example

```c
/* converts a word value to a byte array */
Word inValue = 2345;
Byte outDataArr[2];

if (coTfsWToArr(inValue, outDataArr, 2) != 1)
{
  /* conversion failed */
} /* if */
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
