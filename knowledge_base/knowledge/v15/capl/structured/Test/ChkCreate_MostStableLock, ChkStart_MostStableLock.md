# ChkCreate_MostStableLock, ChkStart_MostStableLock

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostStableLock(Callback aCallback);
dword ChkStart_MostStableLock(Callback aCallback);
```

## Description

The check function monitors the occurrence of "StableLock" events.

A "StableLock" event is generated as soon as the hardware has been in the "Lock" condition for a period of time equal to or longer than tLock (see MOST Specification V 2.4), provided that no "Unlock" events have occurred.

This check always works on events. Therefore, it will not detect a current "StableLock" state, if this state has been entered before the check’s activation.

## Parameters

| Name | Description |
|---|---|
| aCallback | Name of the callback function, which should be called as soon as a "StableLock" event occurs. In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

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
