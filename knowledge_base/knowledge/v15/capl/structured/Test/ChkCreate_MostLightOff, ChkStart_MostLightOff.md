# ChkCreate_MostLightOff, ChkStart_MostLightOff

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostLightOff();
dword ChkStart_MostLightOff();
dword ChkCreate_MostLightOff(Callback aCallback);
dword ChkStart_MostLightOff(Callback aCallback);
```

## Description

The check function monitors the occurrence of "LightOff" events.

A "LightOff" event occurs if the hardware connected to the channel no longer receives light at the input.

## Parameters

| Name | Description |
|---|---|
| aCallback | Name of the callback function, which should be called as soon as a "LightOff" event occurs. In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | — | — | — | — |
| Restricted To | — | MOST | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
