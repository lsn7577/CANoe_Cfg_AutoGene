# J1939AppTxIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppTxIndication( long ecuHandle, long txPG, long source, long dest );
```

## Description

Indicates that a PG has been sent successfully. The function for determining the actual sending time can be useful, especially in the case of a fragmented transfer or higher bus load. Use the function J1939GetRxData() to get the data bytes of the parameter group.

## Return Values

—

## Example

```c
dword J1939AppTxIndication( LONG ecuHdl, LONG txPG, LONG source, LONG dest )
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
