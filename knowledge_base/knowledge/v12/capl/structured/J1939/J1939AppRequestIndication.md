# J1939AppRequestIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppRequestIndication( long ecuHandle, long source, long dest, long page, long pgNum );
```

## Description

This function indicates to the ECU that the "OnRequest" parameter group has been received. The application must respond appropriately (see specification).

It should be noted that this function is only called once for each logical ECU within a node when global PGs are received.

## Return Values

—

## Example

```c
dword J1939AppRequestIndication( LONG ecuHdl, LONG source, LONG dest, LONG page, LONG pgNum)
{
  /* user code */
  return 0;
}
```

## Availability

| Since Version |
|---|
