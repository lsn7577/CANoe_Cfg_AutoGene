# GNSSAddWpS

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpS( double latitude, double longitude, double altitude, double speed )
```

## Description

This function inserts a new waypoint at a given speed at the end of the waypoint list. When this waypoint is reached, the GNSS receiver moves on at the assigned speed. The speed will continue to be used until a waypoint with another speed is reached or the speed is changed by the GNSSSetSpeed function.

The unit of the parameters speed and altitude depends on the system of measurement units selected with the GNSSSetUnits function.

## Parameters

| Name | Description |
|---|---|
| latitude | latitude of the new waypoint in degrees |
| longitude | longitude of the new waypoint in degrees |
| altitude | altitude of the new waypoint (in m or ft) |
| speed | speed of the GNSS receiver (in km/h, mph or kn) |

## Return Values

error code

## Example

```c
// stop GNSS receiver if the following 
 waypoint is reached
GNSSAddWpS( 48.46, 9.11, 255.0, 0 );
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
