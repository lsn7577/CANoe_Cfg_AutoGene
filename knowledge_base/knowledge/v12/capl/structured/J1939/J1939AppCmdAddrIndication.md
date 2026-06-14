# J1939AppCmdAddrIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppCmdAddrIndication( long ecuHandle, long length );
```

## Description

This function indicates that a new address has been assigned to the control device by the "CommandedAddress". The ECU must log on to the bus with the assigned address (see J1939ECUGoOnline()).

Since the PG also returns the name of the ECU, the data must be requested within this callback with J1939GetRxData(). This function is only called, if the ECU can change its address (‚Self Configuring Address‘-Bit of the device name must be set).

## Return Values

—

## Example

```c
dword J1939AppCmdAddrIndication( LONG ecuHandle, LONG length)
{
/* user code */
}
```

## Availability

| Since Version |
|---|
