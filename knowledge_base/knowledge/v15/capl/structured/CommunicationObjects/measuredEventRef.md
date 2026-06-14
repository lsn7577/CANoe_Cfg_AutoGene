# measuredEventRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredEventRef * <var>; // form 1
measuredEventRef <Event> <var>; // form 2
measuredEventRef <Datatype> <var>; // form 3
```

## Description

References an event measurement point, which means measuring a specific connection between consumer and provider for a service event.

## Parameters

| Name | Description |
|---|---|
| Event | Event, determining the data type of the object. |
| Datatype | Data type of the object. |

## Example

```c
measuredEventRef MirrorAdjustment.Position event;
event = MirrorAdjustment.measure[CANoe,LeftMirror].Position;
write("Latest x: %d", $event.x);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
