# diagGetTargetQualifier

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetTargetQualifier( DWORD index, char bufferOut[], DWORD bufferSize);
```

## Description

Writes the target qualifier for the diagnostic target at given index into the buffer. If successful, the qualifier can be used in DiagSetTarget.

## Return Values

Error code or number of characters copied into the buffer. Note that an error is returned if the buffer is too small for the qualifier.

## Example

```c
long i;
char ecuQual[100];
i = diagGetTargetCount();
while( i-- > 0)
{
   diagGetTargetQualifier( i, ecuQual, elcount(ecuQual));
   write( "Target %d: %s", i, ecuQual);
}
```

## Availability

| Since Version |
|---|
