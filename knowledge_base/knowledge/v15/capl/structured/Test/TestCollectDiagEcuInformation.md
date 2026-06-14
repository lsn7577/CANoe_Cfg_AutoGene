# TestCollectDiagEcuInformation

> Category: `Test` | Type: `function`

## Syntax

```c
TestCollectDiagEcuInformation(char class[]); // form 1
TestCollectDiagEcuInformation(char ecuQualifier[], char class[]); // from 2
```

## Description

Sends diagnostic requests to the currently selected diagnostic target or the given ECU and writes the responses to the report file. It considers all requests below a diagnostic class that have constant parameters only.

## Parameters

| Name | Description |
|---|---|
| class | The qualifier of the diagnostic class. |
| ecuQualifier | The qualifier of the ECU. |

## Return Values

Error code

## Example

```c
testcase IdentifyAllEcus()
{
  char ecuQual[200];
  long i;
  i = diagGetTargetCount();
  while( i-- > 0)
  {
    long class;
    long status;
    if( 0 >= diagGetTargetQualifier( i, ecuQual, elcount( ecuQual)))
    {
      TestStepFail( "", "Cannot retrieve qualifier of ECU target %d", i);
      continue;
    }
    write( "Collecting information from target %s", ecuQual);
    status = TestCollectDiagEcuInformation( ecuQual, "Identification");
    if( status == 0)
      TestStepPass( "ECU information collected successfully");
    else
      TestStepFail( "", "Error %d collecting information from ECU %s", status, ecuQual);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP3: form 1 8.2: form 2 | — | — | — | 1.0: form 1 1.1: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
