# J1939ILGetAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILGetAddress(); // form 1
```

## Description

Returns the address that is used by the J1939 IL.

## Example

```c
on key 'a'
{
  LONG addr;
  addr = J1939ILGetAddress();
}
```

## Availability

| Since Version |
|---|
