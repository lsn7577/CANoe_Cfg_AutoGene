# SetControlForeColor

> Category: `Other` | Type: `function`

## Syntax

```c
void SetControlForeColor(char[] panel, char[] control, long color);
```

## Description

Sets the foreground color of:

certain panel controls

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| Note Symbol assignment is not case sensitive. If you want to access all elements of a panel the notation "" is used, see example below. |  |
| Example "Signal:SleepInd""Signal:easy/MotorState/EngineSpeed""SysVar:SysVarTester" (for a system variable defined with name space TestSysvar in the configuration) |  |
| Note for 'CAPL Output View' Control When changing the text color only the following/future output — using putValueToControl — is colored with the new one. The existing output stays unchanged in color. |  |
| Note makeRGB Up to and including CANoe version 12.0 SP2, the function makeRGB returned the blue value in the second byte and the red value in the fourth byte.Functions that received this value as a parameter interpreted this exchange so that the color was displayed correctly. From CANoe 12.0 SP3, the function makeRGB returns the color values in the correct order.Functions that have received this value as a parameter have also been adjusted to display the correct color again. Existing programs only need to be adapted if you have not used the function makeRGB but you have passed the color hard coded. |  |

## Return Values

—

## Example

```c
// Set the foreground color for a specific control of a panel
SetControlForeColor("motor", "PedalPos", MakeRGB(255,0,0));
// All controls of the panel are set to the same foreground color
SetControlForeColor("motor", "", MakeRGB(255,0,0));
// All controls of all panels are set to the same foreground color
SetControlForeColor("", "", MakeRGB(255,0,0));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 4.1 | 13.0 | — | — | 1.0 |
| Restricted To | certain panel controls | certain panel controls | certain panel controls | — | — | certain panel controls |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
