# TestJoinDiagVariantIdentificationCompleted

> Category: `Test` | Type: `function`

## Syntax

```c
long testJoinDiagVariantIdentificationCompleted(char ecuQualifier[]);
```

## Description

Adds an event to the set of joined events that will fire when the variant identification started for the given ECU is completed.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | The event will fire on the completion of the variant identification for this ECU. |

## Return Values

Number of conditions in stock:
Error code

## Example

```c
testcase TC_ParallelIdentification()
{
  // Perform variant identification for 3 ECUs in parallel
  diagStartVariantIdentification("ECU1");
  testJoinDiagVariantIdentificationCompleted("ECU1");
  diagStartVariantIdentification("ECU2");
  testJoinDiagVariantIdentificationCompleted("ECU2");
  diagStartVariantIdentification("ECU3");
  testJoinDiagVariantIdentificationCompleted("ECU3");

  if( 0 < TestWaitForAllJoinedEvents(5000))
  TestStepPass( "All variant identification tasks completed in time.");
  else
  TestStepFail( "Not all variant identification tasks completed in time!");

  {
    char identifiedVariant[100];
    diagGetIdentifiedVariant( "ECU1", identifiedVariant, elcount(identifiedVariant));
    if( 0 == strncmp( identifiedVariant, "Beta", 5))
      TestStepFail( "Should not run this test with beta version!");
  }
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | — | — | — | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
