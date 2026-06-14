# diagInterpretRespAs

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagInterpretRespAs( diagRequest response, char primitiveQualifier[]);
```

## Description

Treats the data of the request's response as the specified primitive. This will cause a reinterpretation of the data, but the data will not be changed.

## Parameters

| Name | Description |
|---|---|
| request | Request that has to contain a response object received by waiting for a response. |
| primitiveQualifier | Qualifier of the service primitive that should be used for reinterpretation. |

## Example

A tester module tries to interpret the response received for a request.

```c
if( 1 == testWaitForDiagResponse( request, 2000))
{ 
   if( 0 == diagInterpretRespAs( request, "ServiEcu1PR"))
   {
      if( 27.5 < diagGetRespParameter( request, "Voltage"))
         TestStepPass( "Voltage is high enough");
      else
         TestStepFail( "Voltage too low");
   } else
   { 
      TestStepFail( "Unexpected response version");
   }
} else
{ 
   TestStepFail( "No response received");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 7.1 SP3 | — | — | — | 1.0 |
| Restricted To | Online mode Not for basic diagnostics | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
