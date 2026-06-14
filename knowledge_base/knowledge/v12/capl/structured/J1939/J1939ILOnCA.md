# J1939ILOnCA

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILOnCA(long newAddress)
```

## Description

This callback function is called from the J1939 IL when a Command Address message is received.

The assignment of the new address can be suppressed.

## Example

```c
long J1939ILOnCA(long address)
{
  if(address == 2)
    return 0; //don’t accept the address ‘2’
  else
    return 1;
}
```

## Availability

| Since Version |
|---|
