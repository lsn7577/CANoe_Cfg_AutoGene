# DoIP_SetVehicleUdpPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleUdpPort( dword port);
```

## Description

Sets the UDP port (UDP_VEHICLE_LOCAL) to be used by the DoIP layer.

This function must be called in on preStart.

## Return Values

—

## Example

```c
dword port;
port = DiagGetCommParameter( "DoIP.VEHICLE_UDP_Data");
// Set the vehicle UDP port
DoIP_SetVehicleUdpPort( port);
```

## Availability

| Since Version |
|---|
