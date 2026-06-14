# measuredMethodRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredMethodRef * <var>; // form 1
measuredMethodRef <Method> <var>; // form 2
measuredMethodRef <Prototype> <var>; // form 3
```

## Description

References a method measurement point, which means measuring a specific connection between consumer and provider for a service function.

## Parameters

| Name | Description |
|---|---|
| Method | Method, determining the data type of the object. |
| Prototype | Data type of the object (a function prototype / signature). |

## Example

```c
measuredMethodRef MirrorAdjustment.Adjust method;
method = MirrorAdjustment.measure[CANoe,LeftMirror].Adjust;
write("Latest x: %d", method.LatestCall.x);
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
