# C2xApplyPathHistory

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xApplyPathHistory(long packet, double latitude, double longitude, double maxDistance) // form 1
long C2xApplyPathHistory(long packet, double latitude, double longitude, double elevation, double maxDistance, long maxPtCount, long routeId) // form 2
```

## Description

This function applies values to multiple path history tokens in the packet. The geographical route of the station (path of the movement) is taken from the scenario route of the station or, when no scenario is applied to this station, from previous calls of the C2xAddGeoPos function. This function applies the path history data to following packet and tokens:

## Parameters

| Name | Description |
|---|---|
| packet | Handle of a packet that has been created with C2xInitPacket or was provided as callback function parameter |
| latitude | New station latitude in degrees, -90.0° < latitude < 90.0° |
| longitude | New station longitude in degrees, -180.0° <= longitude <= 180.0° |
| elevation (optional) | New station altitude in meters, -1000.0m <= elevation <= 8000.0m. Set the elevation parameter to a value outside of the valid range to indicate that the elevation is not provided / is unused. |
| maxDistance | Maximal length in meters of the path history. 0.0m < maxDistance <1000.0m. Set values below 1000 (m) to limit the geographical length of the station path history applied by this function |
| maxPtCount | Maximal count of path history points applied by this function. It is limited by the allowed maximal length of path history sequence token in the database for concrete packet (CAM, DENM, BasicSafetyMessage). |
| routeId | Unique integer number which identify the path history data storage from where the position data will be used. The path history data source here are previous periodic calls to the CAPL Function C2xAddGeoPos with the same value of routeId parameter. Valid value range: routeId > 0. |

## Example

```c
void OnPreTxCAM(LONG packet)
{
  C2xApplyPathHistory(packet, @GPS::GPS1.Latitude, @GPS::GPS1.Longitude, @GPS::GPS1.Altitude, 1000);
  C2xCompletePacket(packet);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
