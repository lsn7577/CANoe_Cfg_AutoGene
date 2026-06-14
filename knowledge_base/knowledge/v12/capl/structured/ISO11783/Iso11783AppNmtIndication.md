# Iso11783AppNmtIndication

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783AppNmtIndication( long busHandle, long address, long flag );
```

## Description

This function is called when an ECU claims n address or an ECU loses its address. The function is also called, if no ECU was created yet.

With Iso11783GetRxData() the device name can be copied to a buffer.

## Return Values

—

## Example

```c
dword Iso11783AppNmtIndication( LONG busHandle, LONG address, LONG flag )
{
  char deviceName[8];
  Iso11783GetRxData( elCount(deviceName), deviceName ); 
  /* user code */
  return 0;
}
```

## Availability

| Since Version |
|---|
