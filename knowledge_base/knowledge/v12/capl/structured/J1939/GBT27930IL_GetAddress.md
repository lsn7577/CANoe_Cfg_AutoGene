# GBT27930IL_GetAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_GetAddress(); // form 1
```

## Description

Returns the address that is used by the GBT27930 IL.

## Example

```c
on key 'a'
{
  LONG addr;
  addr = GBT27930IL_GetAddress();
}
```

## Availability

| Since Version |
|---|
