# DoIP_SetVehicleTcpPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleTcpPort( dword port);
```

## Description

Sets the TCP port (TCP_DATA) to be used by the DoIP layer.

This function must be called in on preStart.

## Return Values

—

## Example

```c
dword port;
port = DiagGetCommParameter( "DoIP.VEHICLE_TCP_Data");
// Set the vehicle TCP port
DoIP_SetVehicleTcpPort( port);
```

## Availability

| Since Version |
|---|
