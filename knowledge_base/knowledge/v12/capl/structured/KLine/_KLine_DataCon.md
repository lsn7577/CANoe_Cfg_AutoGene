# _KLine_DataCon

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_DataCon(long count)
```

## Description

Called for a transmitted K-Line response.

This function models a K-Line TP layer which is required for a ECU simulation.

## Return Values

—

## Example

```c
_KLine_DataCon( long count)
{
   write(%d byte sent", count);
   diag_DataCon( count);
}
```

## Availability

| Since Version |
|---|
