# TestCollectDiagEcuInformation

> Category: `Test` | Type: `function`

## Syntax

```c
TestCollectDiagEcuInformation(char class[]);
```

## Description

Sends diagnostic requests to the currently selected diagnostic target or the given ECU and writes the responses to the report file. It considers all requests below a diagnostic class that have constant parameters only.

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

| Since Version |
|---|
