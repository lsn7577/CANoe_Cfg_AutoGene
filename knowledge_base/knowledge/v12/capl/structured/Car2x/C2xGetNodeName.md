# C2xGetNodeName

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetNodeName(long stationHandle, long length, char name[]);
```

## Description

Get the name of the database node which is assigned to the ITS Station in the StationManager.

## Return Values

0 or error code.

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

| Since Version |
|---|
