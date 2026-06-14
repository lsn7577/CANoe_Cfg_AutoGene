# _DoIP_VehicleIdentificationCompleteInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_VehicleIdentificationCompleteInd();
```

## Description

The vehicle identification phase has completed, i.e. the tester is about to select the vehicle to communicate with. This is called when the timeout A_DoIP_Ctrl (standard: 2 s) expires after a Vehicle Identification Request (VIR) Message has been sent. It is also called when the vehicle responds that is targeted by the VIR message, i.e. before communication with this vehicle is initiated.

## Return Values

—

## Example

```c
void _DoIP_VehicleIdentificationCompleteInd()
{
  write( "[%.3f] _DoIP_VehicleIdentificationCompleteInd, %d vehicles found", timenow()/100000.0, gVehiclesFound);
  if(gVehiclesFound > 1)
  {
    // Select the second vehicle that has responded
    DoIP_SelectVehicle(gVehicleAnswered[gVehiclesFound – 2]);
  }
  // else: a single vehicle will be selected automatically
}
```

## Availability

| Since Version |
|---|
