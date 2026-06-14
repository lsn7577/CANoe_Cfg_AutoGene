# C2xGetStationColor

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetStationColor(long stationHandle);
```

## Description

Retrieve the color associated with the ITS Station in the Station Manager. The ITS Station can be identified by its handle or by the name of the associated node in the database.

## Return Values

The station color encoded as RGB Value (0xBBGGRR).

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

| Since Version |
|---|
