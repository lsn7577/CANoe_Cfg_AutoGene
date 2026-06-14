# AvbListen

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbListen(dword listenerHandle, char onListenCallback[]);
```

## Description

The function causes the Listener to listen for incoming connection requests, which will be provided in the CAPL callback OnAvbListen passed to this function.

The function simultaneously listens for incoming connection requests for streams propagated via the following transport protocols:

Incoming connection requests can be accepted with AvbAccept from inside the provided callback function OnAvbListen.

## Parameters

| Name | Description |
|---|---|
| listenerHandle | The Listener handle. |
| onListenCallback | The name of the CAPL callback function (see OnAvbListen). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2 10.0: RTP via UDP (*) 10.0 SP3: RTSP via TCP (**) | — | — | — | 2.0 SP2 2.2: RTP via UDP (*) 2.2 SP2: RTSP via TCP (**) |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
