# SetControlProperty

> Category: `Other` | Type: `function`

## Syntax

```c
void SetControlProperty(char[] panel, char[] control, char[] property, long value); // from 1
void SetControlProperty(char[] panel, char[] control, char[] property, float value); // fom 2
void SetControlProperty(char[] panel, char[] control, char[] property, char[] value); // from 3
```

## Description

Sets a property of a Panel Designer control.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

It is easier to access color properties by makeRGB.

The following properties and values can be set:

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| control | Name of the panel control, restricted to 128 characters."" – references all elements on the panel. |
| property | Name of the property |
| value | Value to be set (long, float or string value) |

## Return Values

—

## Example

```c
SetControlProperty("Measurements", "StatusIndicator", "Caption", "running");
SetControlProperty("Measurements", "StatusIndicator", "BackColor", MakeRGB(0,145,255));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 4.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
