# VTIL_GetAddress

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetAddress();
```

## Description

Returns the address that is used by the VT IL.

## Return Values

>=0: Address of the VT IL

## Example

```c
on key 'a'
{
  long addr;
  addr = VTIL_GetAddress();
}
```

## Availability

| Since Version |
|---|
