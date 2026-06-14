# diagGetComplexParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetComplexParameter (diagResponse obj, char parameterName[], dword iteration, char subParameter[], char buffer[], dword buffersize)
long diagGetComplexParameter (diagRequest obj, char parameterName[], dword iteration, char subParameter[], char buffer[], dword buffersize)
```

## Description

Returns the symbolic value of a complex parameter. This is possible for all parameters.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| parameterName | Parameter qualifier |
| iteration | Iteration (beginning with 0) |
| subParameter | Sub parameter qualifier |
| buffer | Output buffer |
| buffersize | Buffer size |

## Return Values

Error code

## Example

```c
on diagResponse Door.FaultMemory_ReadAllIdentified
{
  dword DTC;
  char DTCasText[100];
  int i;

  if(diagIsPositiveResponse(this))
  {
    // Iterate over the list of DTCs and retrieve the numeric and symbolic value of each DTC
    for(i=0;i<DiagGetIterationCount(this,"ListOfDTC");i++)
    {
      DTC=DiagGetComplexParameter(this,"ListOfDTC",i,"DTC");
      DiagGetComplexParameter(this,"ListOfDTC", i, "DTC" , DTCasText, elCount(DTCasText));
      write("DTC %06X - %s",DTC, DTCasText);
    }
  }
  else
  {
    write("Negative response received.\nNegative response code: 0x%02X", (byte)DiagGetResponseCode(this));
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 5.0 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | Online mode Not for basic diagnostics | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
