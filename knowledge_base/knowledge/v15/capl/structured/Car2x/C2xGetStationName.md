# C2xGetStationName

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetStationName(long stationHandle, long length, char name[]);
```

## Description

Get the name assigned to the ITS Station in the StationManager.

## Parameters

| Name | Description |
|---|---|
| stationHandle | Handle of the ITS station. |
| length | Maximum number of bytes to be copied. |
| name | Buffer in which the name is copied. |

## Example

```c
char   stationName[1024];
long   stationHdl ;

stationHdl = C2xGetStationHandle(packet) ;
if (C2xGetStationName(stationHdl, elcount(stationName), stationName) == 0)
{
  write("Station: %s", stationName) ;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
