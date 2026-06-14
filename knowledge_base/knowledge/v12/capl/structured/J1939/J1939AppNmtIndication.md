# J1939AppNmtIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppNmtIndication( long busHandle, long address, long flag );
```

## Description

This function is called when an ECU claims n address or an ECU loses its address. The function is also called, if no ECU was created yet.

With J1939GetRxData() the device name can be copied to a buffer.

## Return Values

—

## Example

```c
dword J1939AppNmtIndication( LONG busHandle, LONG address, LONG flag )
{
  char deviceName[8];
  J1939GetRxData( elCount(deviceName), deviceName ); 
  /* user code */
  return 0; 
}
```

## Availability

| Since Version |
|---|
