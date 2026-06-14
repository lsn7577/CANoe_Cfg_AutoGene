# SetDefaultControlColors

> Category: `Other` | Type: `function`

## Syntax

```c
void SetDefaultControlColors(char[] panel, char[] control);
```

## Description

Sets back the background and text color of as defined in the Panel Designer:

certain panel controls

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| Note Symbol assignment is not case sensitive. If you want to access all elements of a panel the notation "" is used, see example below. |  |
| Example "Signal:SleepInd""Signal:easy/MotorState/EngineSpeed""SysVar:SysVarTester" (for a system variable defined with name space TestSysvar in the configuration) |  |
| Note for 'CAPLOutputView' Control When changing the background and text color only the following/future output — using putValueToControl — is colored with the new one. The existing output stays unchanged in color. |  |

## Return Values

—

## Example

```c
//Set the default background and text color for a specific control of a panel.
SetDefaultControlColors("motor", "PedalPos");
//All controls of the panel are set to the default background and text color as defined in the Panel Designer.
SetDefaultControlColors("motor", "");
//All controls of all panels are set to the default background and text color as defined in the Panel Designer.
SetDefaultControlColors("", "");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.5 | 13.0 | — | — | 1.0 |
| Restricted To | certain panel controls | certain panel controls | certain panel controls | — | — | certain panel controls |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
