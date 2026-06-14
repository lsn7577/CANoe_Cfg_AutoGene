# _DoIP_VehicleConnectedInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_VehicleConnectedInd();
```

## Description

The TCP communications channel to the vehicle has been established successfully, i.e. diagnostic messages can be exchanged without further delays.

## Return Values

—

## Example

```c
void _DoIP_VehicleConnectedInd()
{
  write( "Vehicle connected.");
}
```

## Availability

| Since Version |
|---|
