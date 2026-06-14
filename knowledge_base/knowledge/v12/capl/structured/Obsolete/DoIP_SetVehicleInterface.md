# DoIP_SetVehicleInterface

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleInterface( char interface[])
```

## Description

Sets the network interface to be used by the DoIP layer. This function must be called in on preStart.

## Return Values

—

## Example

```c
// Set the network interface
char buffer[256];
DiagGetCommParameter( "DoIP.VEHICLE_Interface",
                      0, buffer, elcount( buffer));
DoIP_SetVehicleInterface( buffer);
```

## Availability

| Since Version |
|---|
