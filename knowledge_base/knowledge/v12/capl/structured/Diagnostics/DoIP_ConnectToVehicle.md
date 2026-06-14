# DoIP_ConnectToVehicle

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_ConnectToVehicle();
```

## Description

Tries to connect to the configured vehicle. A vehicle identification phase may be started to retrieve the vehicle IP address.

## Return Values

—

## Example

```c
// If key is pressed, connect to vehicle
On key 'c'
{
  DoIP_ConnectToVehicle();
}
```

## Availability

| Since Version |
|---|
