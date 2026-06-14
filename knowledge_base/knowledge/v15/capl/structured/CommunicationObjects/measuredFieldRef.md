# measuredFieldRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredFieldRef * <var>; // form 1
measuredFieldRef <Field> <var>; // form 2
measuredFieldRef <Datatype> <var>; // form 3
```

## Description

References a field measurement point, which means measuring a specific connection between consumer and provider for a service field.

## Parameters

| Name | Description |
|---|---|
| Field | Field, determining the data type of the object. |
| Datatype | Data type of the object. |

## Example

```c
measuredFieldRef MirrorAdjustment.Position field;
field = MirrorAdjustment.measure[CANoe,LeftMirror].Position;
write("Latest x: %d", $field.x);
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
