# DoIP_GetVehicleDiscoveryTimeout, DoIP_SetVehicleDiscoveryTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleDiscoveryTimeout(dword toVehicleDiscovery);
```

## Description

Sets or returns the timeout waiting for Vehicle Identification Response Messages after a Vehicle Identification Request was sent (in milliseconds).

## Return Values

Form 1: —Form 2: Timeout waiting for Vehicle Identification Response Messages

## Example

This value can also be configured in the DoIP.INI file.

```c
// Wait longer than the standard suggests to detect more vehicles
DoIP_SetVehicleDiscoveryTimeout( 10000);
```

## Availability

| Since Version |
|---|
