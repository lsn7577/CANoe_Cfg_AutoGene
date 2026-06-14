# SetClockControlTime

> Category: `Other` | Type: `function`

## Syntax

```c
void SetClockControlTime(char[] panel, char[] control, int hours, int minutes, int seconds); // form 1
void SetClockControlTime(char[] panel, char[] control, int time); // form 2
```

## Description

Sets the time of the Panel Designer Clock Control.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| Note Symbol assignment is not case sensitive. If you want to access all elements of a panel the notation "" is used, see example below. |  |
| Example "Signal:SleepInd""Signal:easy/MotorState/EngineSpeed""SysVar:SysVarTester" (for a system variable defined with name space TestSysvar in the configuration) |  |
| hours | Defines the hours of the time to be displayed in the clock control. |
| minutes | Defines the minutes of the time to be displayed in the clock control. |
| seconds | Defines the seconds of the time to be displayed in the clock control. |
| time | Defines the time in seconds to be displayed in the clock control. The corresponding hours, minutes and seconds are calculated during runtime. |

## Return Values

—

## Example

```c
// Set the time in hours, minutes, seconds. It will be displayed '10:20:30'.
on key 'a'
{
SetClockControlTime("ClockControl1", "ClockCAPL", 10, 20, 30);
}
// Set the time in seconds. It will be displayed '01:00:00'.
on key 'b'
{
SetClockControlTime("ClockControl1", "ClockCAPL", 3600);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.5 | 13.0 | — | — | 1.0 |
| Restricted To | Clock Control | Clock Control | Clock Control | — | — | Clock Control |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
