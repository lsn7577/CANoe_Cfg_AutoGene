# J1939AppAddrClaimed

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppAddrClaimed( long ecuHandle );
```

## Description

Indicates that Address Claiming was performed successfully, which means that the control device is permitted to communicate on the CAN bus.

## Return Values

—

## Example

```c
dword J1939AppAddrClaimed( LONG ecuHandle )
{
  /* user code */
  return 0;
}
```

## Availability

| Since Version |
|---|
