# DoIP_SetVehicleAdapter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleAdapter( char adapter[])
```

## Description

Sets the network interface to be used by the DoIP layer.

This function must be called in on preStart.

## Return Values

—

## Example

```c
// Set the network interface
char buffer[256];
DiagGetCommParameter( "DoIP.VEHICLE_Adapter",
                      0, buffer, elcount( buffer));
DoIP_SetVehicleAdapter( buffer);
```

## Availability

| Since Version |
|---|
