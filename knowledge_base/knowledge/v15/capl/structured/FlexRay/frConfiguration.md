# frConfiguration

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frConfiguration <configuration var>;
```

## Description

Can be used to create a FlexRay parameter object. The data content of this object is all protocol parameters relevant to FlexRay in the context of initializing a FlexRay Communication Controller. The object data can be manipulated or read out by selectors associated with this object.

Initially, all protocol parameters are set to a value of 0.

The frGetConfiguration or frSetConfiguration functions are used to read or set parameters from or in the FlexRay interface’s Communication Controller.

## Parameters

| Name | Description |
|---|---|
| <configuration var> | Character string defining the object’s variable name. |

## Example

For an example see functions frGetConfiguration and frSetConfiguration.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.1 | 6.1 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
