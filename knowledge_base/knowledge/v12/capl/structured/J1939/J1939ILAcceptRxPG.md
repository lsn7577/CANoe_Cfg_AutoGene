# J1939ILAcceptRxPG

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILAcceptRxPG( pg * rxPG )
```

## Description

Checks if the received parameter group is addressed to the J1939 IL.

## Example

```c
on pg TPRS
{
  if (J1939ILAcceptRxPG( this ) <= 0) return;
  // ...
}
```

## Availability

| Since Version |
|---|
