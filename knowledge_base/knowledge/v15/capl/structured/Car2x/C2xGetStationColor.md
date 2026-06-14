# C2xGetStationColor

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetStationColor(long stationHandle);
long C2xGetStationColor(char dbNodeName[]);
```

## Description

Retrieve the color associated with the ITS Station in the Station Manager. The ITS Station can be identified by its handle or by the name of the associated node in the database.

## Parameters

| Name | Description |
|---|---|
| stationHandle | Handle of the ITS station. |
| dbNodeName | Name of the database node associated with the station. Note: CAPL Macro %NODE_NAME% can be used as value for the dbNodeName parameter to get the station color for a calling ECU CAPL node. |

## Example

```c
on key 'c'
{
  long stationColor;
  stationColor = C2xGetStationColor("%NODE_NAME%");
  write ("Station %NODE_NAME% color : 0x%X", stationColor);
}

void OnC2xPacket (LONG channel, LONG dir, LONG radioChannel, 
LONG signalStrength, LONG sigQuality, LONG packet)
{
  long rxStationHdl;
  long stationColor;

  rxStationHdl = C2xGetStationHandle(packet);
  stationColor = C2xGetStationColor(rxStationHdl);
  stationColor = C2xGetStationColor("DUT");
  stationColor = C2xGetStationColor("%NODE_NAME%");
  write ("Station color: 0x%X", stationColor);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP4 | — | — | — | 2.2 SP4 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
