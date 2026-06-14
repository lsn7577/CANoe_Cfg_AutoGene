# VTIL_AcceptRxPG

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_AcceptRxPG( pg * rxPG );
```

## Description

Checks if the received parameter group is addressed to the ISO11783 IL.

## Return Values

<0: VT IL Error Code

## Example

```c
on pg TPRS
{
  if (VTIL_AcceptRxPG( this ) <= 0) return;
  // ...
}
```

## Availability

| Since Version |
|---|
