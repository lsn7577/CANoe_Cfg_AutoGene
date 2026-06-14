# Iso11783AppRxIndication

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783AppRxIndication( long ecuHandle, long srcAddr, long dstAddr, long length, long pgnum );
```

## Description

The callback function indicates to the user that a parameter group has been received. It is not possible in CAPL to receive PG data through a callback function. For this reason, the data must be explicitly requested within the callback function with Iso11783GetRxData().

It should be noted that this function is only called once for each logical ECU within a node when global PGs are received.

## Return Values

—

## Example

```c
dword Iso11783AppRxIndication( LONG ecuHdl, LONG srcAddr, LONG dstAddr, LONG len, LONG pgNumber)
{
  char data[50];
  Iso11783GetRxData( elCount(data), data );
  /* user code */
  return 0;
}
```

## Availability

| Since Version |
|---|
