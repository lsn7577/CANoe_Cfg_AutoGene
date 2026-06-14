# diagGetTargetQualifier

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetTargetQualifier( DWORD index, char bufferOut[], DWORD bufferSize);
```

## Description

Writes the target qualifier for the diagnostic target at given index into the buffer. If successful, the qualifier can be used in DiagSetTarget.

## Parameters

| Name | Description |
|---|---|
| index | Value in 0 ≤ index ≤ n, where /n/ is the number of possible targets returned by DiagGetTargetCount. |
| bufferOut | Character array for the result. |
| bufferSize | Maximum number of characters available in the buffer. |

## Return Values

Error code or number of characters copied into the buffer. Note that an error is returned if the buffer is too small for the qualifier.

## Example

```c
long i;
char ecuQual[100];
i = diagGetTargetCount();
while( i-- > 0)
{
   diagGetTargetQualifier( i, ecuQual, elcount(ecuQual));
   write( "Target %d: %s", i, ecuQual);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 7.5 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
