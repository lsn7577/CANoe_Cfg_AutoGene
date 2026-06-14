# FSIL_GetAddress

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_GetAddress(); // form 1
```

## Description

Returns the address that is used by the FS IL.

## Return Values

>=0: Address of the FS IL

## Example

```c
on key 'a'
{
  long addr;
  addr = FSIL_GetAddress();
}
```

## Availability

| Since Version |
|---|
