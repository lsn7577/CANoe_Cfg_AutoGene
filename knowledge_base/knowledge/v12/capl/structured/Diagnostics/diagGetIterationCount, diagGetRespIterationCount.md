# diagGetIterationCount, diagGetRespIterationCount

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetIterationCount( diagRequest obj, char complexParamQualifier[]);
long diagRequest::GetIterationCount( char complexParamQualifier[]);
```

## Description

Returns the number of sub-parameter iterations the complex parameter holds.

## Return Values

If >= 0 the number of iterations, otherwise an error code.

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

| Since Version |
|---|
