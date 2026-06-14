# GNSSAddWpLine

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpLine( double latitude1, double longitude1, double altitude1, double latitude2, double longitude2, double altitude2,dword straightLine)
```

## Description

This function can be used to describe a line. To do this, the points that describe the line are inserted at the end of the waypoint list.

StraightLine = 1

StraightLine = 0

The unit of the parameters altitude1 and altitude2 depends on the system of measurement units selected with the GNSSSetUnits function.

## Parameters

| Name | Description |
|---|---|
| latitude1 | latitude of the waypoint at the beginning of the line (in degrees) |
| longitude1 | longitude of the waypoint at the beginning of the line (in degrees) |
| altitude1 | altitude of the waypoint at the beginning of the line (in m or ft) |
| latitude2 | latitude of the waypoint at the end of the line (in degrees) |
| longitude2 | longitude of the waypoint at the end of the line (in degrees) |
| altitude2 | altitude of the waypoint at the end of the line (in m or ft) |
| straightLine | 1 if the two points are connected by a straight line, otherwise 0 |

## Return Values

error code

## Example

```c
GNSSAddWpLine( 54.0, 8.0, 0.0, 54.2, 7.9, 0.0, 1 );
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
