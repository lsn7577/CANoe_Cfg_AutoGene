# J1939AppRxIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppRxIndication( long ecuHandle, long srcAddr, long dstAddr, long length, long pgnum );
```

## Description

The callback function indicates to the user that a parameter group has been received. It is not possible in CAPL to receive PG data through a callback function. For this reason, the data must be explicitly requested within the callback function with J1939GetRxData().

It should be noted that this function is only called once for each logical ECU within a node when global PGs are received.

## Return Values

—

## Example

```c
dword J1939AppRxIndication( LONG ecuHdl, LONG srcAddr, LONG dstAddr, LONG len, LONG pgNumber)
{
  char data[50];
  J1939GetRxData( elCount(data), data );
  /* user code */
  return 0;
}
```

## Availability

| Since Version |
|---|
