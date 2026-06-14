# diagGetTargetCount

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetTargetCount();
```

## Description

Returns the number /n/ of possible diagnostic targets configured. For indices /i/ with 0 ≤ i ≤ n you can retrieve the target qualifier with DiagGetTargetQualifier.

Diagnostic descriptions that cannot work as diagnostic targets are not counted, e.g. descriptions configured as interpretation only are ignored.

## Return Values

Error code or number of diagnostic targets.

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
