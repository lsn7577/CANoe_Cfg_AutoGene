# C2xAddGeoPos

> Category: `Car2x` | Type: `function`

## Syntax

```c
C2xAddGeoPos(double latitude, double longitude, double elevation, double heading, double speed // form 1
C2xAddGeoPos(double latitude, double longitude, double elevation, double heading, double speed, double hdop, double vdop, long routeId) // form 2
```

## Description

This function sets the current geographical position of the station. As soon as a new geographical position is available, this function should be called again. The following data sources can usually provide the required geographical position continuously (see CAPL examples below):

The recommended frequency of updating the station position data by calling this function is 100ms, maximum 1000ms.

## Parameters

| Name | Description |
|---|---|
| latitude | New station latitude in degrees, -90.0° < latitude < 90.0° |
| longitude | New station longitude in degrees, -180.0° <= longitude <= 180.0° |
| elevation | Optional, new station altitude in meters, -1000.0m <= elevation <= 8000.0m. Set the elevation parameter to a value outside of the valid range to indicate that the elevation is not provided / is unused. |
| heading | New station heading angle, in degrees from north, 0.0° <= heading <= 360.0° |
| speed | New station speed in m/s, speed >= 0.0 |
| hdop (optional) | New value for horizontal dilution of precision, supplied by most GNSS receivers (see sample CAPL code below), 0.1 < hdop < 100.0. Values below 5.0 mean the GNSS fix is of good quality. Provide a negative value to this parameter to indicate that the hdop parameter is not provided / is unused. |
| vdop (optional) | New value for vertical dilution of precision, supplied by most GNSS receivers (see sample CAPL code below), 0.1 < vdop < 100.0. Values below 5.0 mean the GNSS fix is of good quality. Provide a negative value to this parameter to indicate that the vdop parameter is not provided / is unused. |
| routeId | Unique integer number which identify the geographical route data storage where the position data will be saved to. In this way the position data of multiple geographical position data sources can be saved separately. By using the same routeId value in e.g. C2xApplyPathHistory CAPL Function the position data of exactly this routeId will be used independent from other existing routes. Valid value range: routeId > 0. |

## Example

```c
// Station geo position source: VN4610, GNSS1
on sysvar GNSS::Ath1
{
  C2xAddGeoPos(
    @GNSS::Ath1.Latitude, @GNSS::Ath1.Longitude,
    @GNSS::Ath1.Altitude, @GNSS::Ath1.Direction,
    @GNSS::Ath1.Speed, @GNSS::Ath1.HDOP, @GNSS::Ath1.VDOP, 0);
}
// Station geo position source: GPS1
on sysvar GPS::GPS1
{
  C2xAddGeoPos(
    @GPS::GPS1.Latitude, @GPS::GPS1.Longitude,
    @GPS::GPS1.Altitude, @GPS::GPS1.Direction,
    @GPS::GPS1.Speed);
}
on key 'x'
{
  long packet;
  double eventPosLat, eventPosLon, eventPosElev;

  C2xResetPathHistory(1);
  C2xAddGeoPos(48.8237712698464, 9.09292418308236, 305, 175, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8236696458096, 9.09293726987592, 305, 179, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8235561291779, 9.09293974544715, 305, 179, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8234426125462, 9.09294222101838, 305, 215, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8234123413672, 9.09290937947773, 305, 195, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8233593667587, 9.09288639039933, 305, 170, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8232944998153, 9.09290281116963, 305, 131, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8232631474293, 9.09295699971161, 305, 97, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8232534173725, 9.09307194510373, 305, 58, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8232836886499, 9.09314748064715, 305, 51, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8233193654869, 9.09321644788235, 305, 75, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8233485556073, 9.09338229766242, 305, 67, 5.5, -1, -1, 1);
  C2xAddGeoPos(48.8233777457107, 9.09348903266938, 305, 86, 5.5, -1, -1, 1);

  eventPosLat = 48.8233831512772;
  eventPosLon = 9.093631893371;
  eventPosElev = 305;

  packet = C2xInitPacket("DENM");
  C2xSetTokenInt(packet, "DENM", "denm.situation.eventType.causeCode", 91); // VehicleBreakDown
  C2xSetTokenPhys(packet, "DENM", "denm.management.eventPosition.latitude", eventPosLat);
  C2xSetTokenPhys(packet, "DENM", "denm.management.eventPosition.longitude", eventPosLon);
  C2xSetTokenPhys(packet, "DENM", "denm.management.eventPosition.altitude.altitudeValue", eventPosElev);

  C2xApplyPathHistory(packet, eventPosLat, eventPosLon, 305, 800, 20, 1);

  C2xCompletePacket(packet);
  C2xOutputPacket(packet);
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
