# Iso11783AppCmdAddrIndication

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783AppCmdAddrIndication( long ecuHandle, long length );
```

## Description

This function indicates that a new address has been assigned to the control device by the "CommandedAddress". The ECU must log on to the bus with the assigned address (see Iso11783ECUGoOnline()).

Since the PG also returns the name of the ECU, the data must be requested within this callback with Iso11783GetRxData(). This function is only called, if the ECU can change its address (‚Self Configuring Address‘-Bit of the device name must be set).

## Return Values

—

## Example

```c
dword Iso11783AppCmdAddrIndication( LONG ecuHandle, LONG length)
{
  /* user code */
  return 0;
}
```

## Availability

| Since Version |
|---|
