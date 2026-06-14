# TestJoinDiagVariantIdentificationCompleted

> Category: `Test` | Type: `function`

## Syntax

```c
long testJoinDiagVariantIdentificationCompleted(char ecuQualifier[]);
```

## Description

Adds an event to the set of joined events that will fire when the variant identification started for the given ECU is completed.

## Return Values

Number of conditions in stock:
-100: Input parameter error, i.e. the variant identification is not running for this ECU.
-3: Error while adding the specified event to the set of joined events.
-1: General error, for example, functionality is not available.
>0: Number of the newly joined event.

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

| Since Version |
|---|
