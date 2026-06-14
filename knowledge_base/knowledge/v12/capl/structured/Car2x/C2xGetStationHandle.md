# C2xGetStationHandle

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetStationHandle(long packetHandle);
```

## Description

Retrieve an ITS Station handle associated with a received packet or a database node. The handle can be used as input for the other functions of the Station API.

## Return Values

Station handle or 0 if not available or on failure.

## Example

```c
void OnC2xPacket (LONG channel, LONG dir, LONG radioChannel, LONG signalStrength, LONG sigQuality, LONG packet)
{
  long rxStationHdl;
  long dbStationHdl;

  rxStationHdl = C2xGetStationHandle(packet);
  dbStationHdl = C2xGetStationHandle("nodename");
}
```

## Availability

| Since Version |
|---|
