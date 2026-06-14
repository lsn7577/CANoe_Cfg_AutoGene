# frGwBypassDynamic

> Category: `FlexRay` | Type: `function`

## Syntax

```c
long frGwBypassDynamic(long bypass, long channel);
```

## Description

Activates/deactivates the automatic routing for the dynamic part. The function can not be used during a measurement.

Settings from the Network Hardware Configuration dialog are overwritten with this function.

## Parameters

| Name | Description |
|---|---|
| bypass | 0 = Routing deactivated1 = Routing activated |
| channel | Output channel of the gateway. |

## Example

```c
...
frGwBypassDynamic (0,1)
// The gateway routing for the dynamic part will be deactivated 
// for the gateway that uses channel 1.
...
```

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
