# diagGetAbsolutePosition, diagGetAbsolutePositionResp

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetAbsolutePosition( diagRequest request, char parameterPath[] , dword& bytePosOut, dword& bitPosOut, dword& bitConsumptionOut); // form 1
long DiagGetAbsolutePosition( diagResponse response, char parameterPath[] , dword& bytePosOut, dword& bitPosOut, dword& bitConsumptionOut); // form 2
long DiagGetAbsolutePositionResp( diagRequest request, char parameterPath[] , dword& bytePosOut, dword& bitPosOut, dword& bitConsumptionOut); // form 3
long DiagGetAbsolutePosition( diagRequest request, char complexParam[], dword iteration , char leafParameter[], dword& bytePosOut, dword& bitPosOut, dword& bitConsumptionOut); // form 4
long DiagGetAbsolutePosition( diagResponse response, char complexParam[], dword iteration , char leafParameter[], dword& bytePosOut, dword& bitPosOut, dword& bitConsumptionOut); // form 5
long DiagGetAbsolutePositionResp( diagRequest request, char complexParam[], dword iteration , char leafParameter[], dword& bytePosOut, dword& bitPosOut, dword& bitConsumptionOut); // form 6
```

## Description

Retrieves the position of a parameter in its primitive. The parameter may be located in a specific iteration in the primitive (forms 4-6) or in the response stored for a request (forms 3 and 6).

## Parameters

| Name | Description |
|---|---|
| request, response | Objekt in which the parameters are located. |
| parameterPath | Path of the parameter in the primitive (forms 1-3). |
| complexParam | Complex parameter (forms 4-6). |
| iteration | Iteration within the complex parameter that is referenced (forms 4-6). |
| leafParameter | Leaf parameter within the referenced iteration in the complex parameter (forms 4-6). |
| bytePosOut | Returns the position of the first byte of the parameter in the primitive. |
| bitPosOut | Returns the number of the bit in the first byte where the parameter starts. |
| bitConsumptionOut | Returns the length of the parameter in bits. |

## Example

```c
{
  dword bytePos;
  dword bitPos;
  dword bitLen;

if( 0 == this.GetAbsolutePosition( "SpecialParameter", bytePos, bitPos, bitLen))
  write( "Special parameter is located at [%u:%u], bytePos, bitPos);
else
  write( "Special parameter is not located in response primitive.");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | — | — | — | 2.2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
