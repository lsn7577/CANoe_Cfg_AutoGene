# Iso11783IL_OnCA

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OnCA(long newAddress);
```

## Description

This callback function is called from the ISO11783 IL when a Command Address message is received.

The assignment of the new address can be suppressed.

## Return Values

1: Accept the new address

## Example

```c
long Iso11783IL_OnCA(long address)
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
