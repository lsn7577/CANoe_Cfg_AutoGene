# VTIL_OnCA

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_OnCA(long newAddress);
```

## Description

This callback function is called from the VT IL when a Command Address message is received.

The assignment of the new address can be suppressed.

## Return Values

1: Accept the new address

## Example

```c
long VTIL_OnCA(long address)
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
