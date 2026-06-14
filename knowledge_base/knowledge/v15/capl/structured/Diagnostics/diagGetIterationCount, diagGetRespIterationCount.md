# diagGetIterationCount, diagGetRespIterationCount

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetIterationCount( diagRequest obj, char complexParamQualifier[]);
long diagGetIterationCount( diagResponse obj, char complexParamQualifier[]);
long diagGetRespIterationCount( diagRequest obj, char complexParamQualifier[]);
```

## Description

Returns the number of sub-parameter iterations the complex parameter holds.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostic object. |
| complexParamQualifier | Qualifier of the complex parameter that holds an iteration. |

## Example

```c
testcase TC_ReadFaultMemory()
{
  diagRequest FaultMemory_ReadAllIdentified req;
  long count;
  req.SendRequest();
  TestWaitForDiagResponse( req, 1000);

  count = req.GetRespIterationCount( "ListOfDTC");
  while( count -- > 0)
  write( "DTC%d = %06x", count, req.GetComplexRespParameter( "ListOfDTC", count, "DTC"));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP3 | 9.0 SP3 | — | — | — | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
