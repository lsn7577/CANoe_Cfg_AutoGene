# DeleteControlContent

> Category: `Other` | Type: `function`

## Syntax

```c
void DeleteControlContent(char[] panel, char[] control);
```

## Description

Deletes the content of the Panel DesignerCAPL Output View.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| control | Name of the CAPL Output View control, restricted to 128 characters."" – references all CAPL Output View controls on the panel. |

## Return Values

—

## Example

```c
// Deletes the contents of a specific CAPL Output View control in the panel motor
DeleteControlContent(„motor“, „Outputview“);
// Deletes the contents of all CAPL Output View controls in the panel motor
DeleteControlContent(„motor“, „“);
// Deletes the contents of all CAPL Output View controls in all panels
DeleteControlContent(„“, „“);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.5 | 13.0 | — | — | 1.0 |
| Restricted To | CAPL Output View | CAPL Output View | CAPL Output View | — | — | CAPL Output View |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
