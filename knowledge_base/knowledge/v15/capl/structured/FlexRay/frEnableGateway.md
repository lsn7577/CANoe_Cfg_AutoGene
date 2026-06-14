# frEnableGateway

> Category: `FlexRay` | Type: `function`

## Syntax

```c
long frEnableGateway(long channelA, long channelB);
```

## Description

Activates the gateway.

Settings from the CANoeNetwork-Hardware-Configuration dialog will be overwritten with this function.

## Parameters

| Name | Description |
|---|---|
| channelA | Channel 1 of the gateway |
| channelB | Channel 2 of the gateway |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 | 8.0 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay On Pre Start | FlexRay On Pre Start | FlexRay On Pre Start | — | — | FlexRay On Pre Start |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
