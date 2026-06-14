# diagGetAbsolutePosition, diagGetAbsolutePositionResp

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetAbsolutePosition( diagRequest request, char parameterPath[] , dword& bytePosOut, dword& bitPosOut, dword& bitConsumptionOut); // form 1
```

## Description

Retrieves the position of a parameter in its primitive. The parameter may be located in a specific iteration in the primitive (forms 4-6) or in the response stored for a request (forms 3 and 6).

## Example

```c
{
  dword bytePos;
  dword bitPos;
  dword bitLen;

if( 0 == this.GetAbsolutePosition( "SpecialParameter", bytePos, bitPos, bitLen))
  write( "Special parameter is located at [%u:%u], bytePos, bitPos);
else
  write( "Special parameter is not located in response primitive.");
}
```

## Availability

| Since Version |
|---|
