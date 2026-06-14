# providedMethodRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedMethodRef * <var>; // form 1
providedMethodRef <Method> <var>; // form 2
providedMethodRef <Prototype> <var>; // form 3
```

## Description

References a provided method endpoint, which means a specific combination of consumer and provider for a service function on provider side.

## Parameters

| Name | Description |
|---|---|
| Method | Method, determining the data type of the object. |
| Prototype | Data type of the object (a function protoype / signature). |

## Example

```c
providedMethodRef MirrorAdjustment.Adjust method1;
method1 = MirrorAdjustment.providerSide[CANoe,LeftMirror].Adjust;
$method1.AutoAnswerTimeNS = ADJUST_DEFAULT_ANSWER_TIME;
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
