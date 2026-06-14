# diagInterpretAs

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagInterpretAs( diagResponse response, char primitiveQualifier[]);
```

## Description

Treats the data of the response object as the specified primitive. This will cause a reinterpretation of the data, but the data will not be changed.

## Parameters

| Name | Description |
|---|---|
| response | Diagnostics object |
| primitiveQualifier | Qualifier of the service primitive that should be used for reinterpretation. |

## Example

This function determines the actual response primitive by trying to set the interpretation of the argument to the defined variations. 0 is returned if interpretation is possible.

```c
long FindCorrectInterpretation( diagResponse * response)
{
   if( !response.InterpretAs( "ServiPR"))
      return 0; // no error -> interpretation OK
   if( !response.InterpretAs( "ServiEcu1PR"))
      return 0; // no error -> interpretation OK
   if( !response.InterpretAs( "ServiDefauD"))
      return 0; // no error -> interpretation OK
   // None of the known primitives matches, so return failure
   return -1; // not found
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 7.1 SP3 | — | — | — | 1.0 |
| Restricted To | Online mode Not for basic diagnostics | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
