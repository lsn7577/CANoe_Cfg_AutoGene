# Iso11783AppAddrClaimed

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783AppAddrClaimed( long ecuHandle );
```

## Description

Indicates that Address Claiming was performed successfully, which means that the control device is permitted to communicate on the CAN bus.

## Return Values

—

## Example

```c
dword Iso11783AppAddrClaimed( LONG ecuHandle )
{
  /* user code */
  return 0;
}
```

## Availability

| Since Version |
|---|
