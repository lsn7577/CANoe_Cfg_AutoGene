# TCIL_AcceptRxPG

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_AcceptRxPG( pg * rxPG );
```

## Description

Checks if the received parameter group is addressed to the TC IL.

## Return Values

<0: TC IL Error Code

## Example

```c
on pg TPRS
{
  if (TCIL_AcceptRxPG( this ) <= 0) return;
  // ...
}
```

## Availability

| Since Version |
|---|
