# C2xGetStationName

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetStationName(long stationHandle, long length, char name[]);
```

## Description

Get the name assigned to the ITS Station in the StationManager.

## Return Values

0 or error code.

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

| Since Version |
|---|
