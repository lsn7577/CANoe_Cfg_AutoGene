# TCIL_GetAddress

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetAddress(); // form 1
```

## Description

Returns the address that is used by the TC IL.

## Return Values

>=0: Address of the TC IL

## Example

```c
on key 'a'
{
  long addr;
  addr = TCIL_GetAddress();
}
```

## Availability

| Since Version |
|---|
