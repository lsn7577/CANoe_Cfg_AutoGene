# GNSSSetRefPoint

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetRefPoint( double latitude, double longitude, double altitude )
```

## Description

This function defines a reference point that will be used by the functions GNSSAddWpRef and GNSSAddWpRefS to calculate a new waypoint. The unit of the altitude parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Parameters

| Name | Description |
|---|---|
| latitude | latitude of the reference point in degrees |
| longitude | longitude of the reference point in degrees |
| altitude | altitude of the reference point (in m or ft) |

## Return Values

error code

## Example

```c
GNSSSetRefPoint( 48.46, 9.11, 225.0 );
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
