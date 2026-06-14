# diagIsValidValue

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsValidValue( diagResponse response, char[] parameterQualifier, long[] errorLevelOut);
```

## Description

Returns 1 if the parameter in the response object is valid, otherwise 0 is returned and the level of the problem (error or warning) is set in the output parameter field.

## Parameters

| Name | Description |
|---|---|
| response | The response object where the parameter is searched |
| parameterQualifier | The qualifier of the parameter that is checked |
| errorLevelOut | Return value if parameter could be checked: errorLevelOut[0]:0: Value is valid1: Warning2: Error |

## Example

```c
on diagResponse Example_Service
{
   long errorLevelOut[1];
   long status;
   status = diagIsValidValue( this, "MyParameter", errorLevelOut);
   if( status == 1)
   {
      write( "Parameter value OK");
   } else if( status == 0)
   {
      if( errorLevelOut[0] == 1)
         write( "Warning.");
      else if( errorLevelOut[0] == 2)
         write( "ERROR!");
   } else
   {
      write( "Error %d checking parameter value!", status);
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.0 |
| Restricted To | — | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
