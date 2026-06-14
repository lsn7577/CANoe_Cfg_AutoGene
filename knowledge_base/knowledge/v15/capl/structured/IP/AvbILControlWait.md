# AvbILControlWait

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbILControlWait();
```

## Description

Stops sending AVB/TSN related messages.

Open Talkers and Listeners are not closed and the time aware end station (PTP clock instance) continues to run. Stream content continues to be received by the AVB IL and can be evaluated. Talkers suppress their automatic stream perpetuation which means they do not fill gaps by sending zero samples when no AvbSend calls are made through CAPL.

Use AvbILControlResume to enable message sending behaviour again.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
