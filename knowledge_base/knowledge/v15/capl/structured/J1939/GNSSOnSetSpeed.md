# GNSSOnSetSpeed

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSOnSetSpeed( double speed )
```

## Description

This function is called if the speed of the simulation has been changed. This is helpful in the case of simulation by a file when the speed is determined from the file (see GNSSStartSimulation).

The unit of the parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Parameters

| Name | Description |
|---|---|
| speed | New speed (in km/h, mph or kn) |

## Return Values

—

## Example

```c
void GNSSOnSetSpeed( double speed )
{
  write(“New speed = %lf”, speed )
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
