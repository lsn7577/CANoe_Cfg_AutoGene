# FSIL_AcceptRxPG

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_AcceptRxPG( pg * rxPG );
```

## Description

Checks if the received parameter group is addressed to the FS IL.

## Return Values

<0: FS IL Error Code

## Example

```c
on pg TPRS
{
  if (FSIL_AcceptRxPG( this ) <= 0) return;
  // ...
}
```

## Availability

| Since Version |
|---|
