# C2xRegisterCallback

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xRegisterCallback(long callbackType, char* callbackFunction);
long C2xRegisterCallback(long callbackType, char* callbackFunction, char* dbMessage);
```

## Description

Register a callback function.

The callback can be registered for all or for a specific message. If the dbMessage parameter is present, the function can be called earliest in the On Start event handler. With multiple calls of this function it is possible to register several callback functions for the same message or to register the same callback function for several messages.

## Parameters

| Name | Description |
|---|---|
| callbackType | 0: Register a Receive Indication callback 1: Register a Pre Transmit Indication callback |
| dbMessage | Name of a database message for which the callback is invoked. |

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
