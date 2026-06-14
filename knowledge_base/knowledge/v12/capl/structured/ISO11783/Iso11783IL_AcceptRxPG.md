# Iso11783IL_AcceptRxPG

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_AcceptRxPG( pg * rxPG );
```

## Description

Checks if the received parameter group is addressed to the ISO11783 IL.

## Return Values

<0: Error code

## Example

```c
on pg TPRS
{
  if (Iso11783IL_AcceptRxPG( this ) <= 0) return;
  // ...
}
```

## Availability

| Since Version |
|---|
