# Iso11783IL_GetAddress

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_GetAddress();
```

## Description

Returns the address that is used by the ISO11783 IL.

## Return Values

>=0: Address of the ISO11783 IL

## Example

```c
on key 'a'
{
  LONG addr;
  addr = Iso11783IL_GetAddress();
}
```

## Availability

| Since Version |
|---|
