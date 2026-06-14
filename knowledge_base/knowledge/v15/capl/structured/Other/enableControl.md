# enableControl

> Category: `Other` | Type: `function`

## Syntax

```c
void enableControl(char panel[], char control[], long enable);
```

## Description

Selective activation and deactivation of:

certain panel controls

If a control and display element is configured as a simple display, this command will have no effect on the element in question.The turned on or turned off state of an element remains intact at the start/end of the measurement. Because of this, a defined state should be created for the beginning of the measurement for the elements involved (for example in the CAPL program under System->Start).

## Parameters

| Name | Description |
|---|---|
| panel | Name of the panel, restricted to 128 characters. If an empty string is transferred, the action will affect all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| Note Symbol assignment is not case sensitive. If you want to access all elements of a panel the notation "" is used, see example below. When a GroupBox or TabControl is activated/deactivated, all controls in the GroupBox or TabControl are also activated/deactivated. See example below. |  |
| Example "Signal:SleepInd""Signal:easy/MotorState/EngineSpeed""SysVar:SysVarTester" (for a system variable defined with name space TestSysvar in the configuration) |  |
| 0 | turn off (disable) |
| 1 | turn on (enable) |

## Return Values

—

## Example

```c
on key 'a'
{
// enables a specific control of the "motor" panel
enableControl("motor", "PedalPos", 1);

// enables all controls of the panel
enableControl("motor", "", 1);

//disables the GroupBox and all controls in the GroupBox:
enableControl("Controlpanel", "LightGroupBox", 0);

//disables the TabControl and all controls on the TabControl:
enableControl("DisplayPanel", "TabControl1", 0);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 4.1 | 13.0 | — | — | 1.0 |
| Restricted To | certain panel controls | certain panel controls | certain panel controls | — | — | certain panel controls |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
