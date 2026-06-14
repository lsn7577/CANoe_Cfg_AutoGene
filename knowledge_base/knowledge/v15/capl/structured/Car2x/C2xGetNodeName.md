# C2xGetNodeName

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetNodeName(long stationHandle, long length, char name[]);
```

## Description

Get the name of the database node which is assigned to the ITS Station in the StationManager.

## Parameters

| Name | Description |
|---|---|
| stationHandle | Handle of the ITS station. |
| length | Maximum number of bytes to be copied. |
| name | Buffer in which the name is copied. In case no database node is assigned to the ITS station the returned string is empty. |

## Example

```c
char   nodeName[1024];
long   stationHdl ;

stationHdl = C2xGetStationHandle(packet) ;
if (C2xGetNodeName(stationHdl, elcount(nodeName), nodeName) == 0)
{
  if (nodeName[0] != 0)
  {
    write("Node: %s", nodeName) ;
  }
  else
  {
    write("Node: no database node assigned") ;
  }
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
