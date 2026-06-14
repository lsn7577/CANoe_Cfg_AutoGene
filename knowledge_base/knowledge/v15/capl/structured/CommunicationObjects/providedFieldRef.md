# providedFieldRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedFieldRef * <var>; // form 1
providedFieldRef <Field> <var>; // form 2
providedFieldRef <Datatype> <var>; // form 3
```

## Description

References a provided field endpoint, which means a specific combination of consumer and provider for a service field on provider side.

## Parameters

| Name | Description |
|---|---|
| Field | A field of a service, determining the data type of the object |
| DataType | The data type of the object |

## Example

```c
providedFieldRef long field1;
field1 = MirrorAdjustment.providerSide[CANoe,LeftMirror].CurrentPosition;
$field1 = newValue;
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
