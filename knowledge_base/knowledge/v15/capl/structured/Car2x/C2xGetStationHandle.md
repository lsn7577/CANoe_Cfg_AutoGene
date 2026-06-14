# C2xGetStationHandle

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetStationHandle(long packetHandle);
long C2xGetStationHandle(char *dbNodeName);
```

## Description

Retrieve an ITS Station handle associated with a received packet or a database node. The handle can be used as input for the other functions of the Station API.

## Parameters

| Name | Description |
|---|---|
| packetHandle | Handle of the received packet. This function is only usable in a CAPL callback that had been registered with C2xReceivePacket or with C2xRegisterCallback for Receive Indications. |
| dbNodeName | Name of a database node. Returns the handle of the station which is assigned to the database node in the StationManager. |

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
