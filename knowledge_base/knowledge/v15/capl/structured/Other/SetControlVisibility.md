# SetControlVisibility

> Category: `Other` | Type: `function`

## Syntax

```c
void SetControlVisibility(char[] panel, char[] control, long visible);
```

## Description

Sets the visibility of all panel controls.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| Note If you want to access all elements of a panel the notation "" is used, see example below. |  |
| Example "Signal:SleepInd""SysVar:SVInteger" |  |
| visible | Sets if the panel element should be visible or not. visible = 1 => Panel element is visiblevisible = 0 => Panel element is not visible |

## Return Values

—

## Example

```c
// Set the visibility for a specific control of a panel
SetControlVisibility("motor", "PedalPos", 1);
// All controls of the panel are set to not visible
SetControlVisibility("motor", "", 0);
// All controls of all panels are set to visible
SetControlVisibility("", "", 1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 8.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
