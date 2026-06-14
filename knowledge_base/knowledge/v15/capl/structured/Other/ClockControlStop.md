# ClockControlStop

> Category: `Other` | Type: `function`

## Syntax

```c
void ClockControlStop(char[] panel, char[] control);
```

## Description

Stops the Clock Control designed as stop watch with the Panel Designer (setting Mode = StopWatch).

The displayed time stays unchanged unless the user starts the stop watch again or resets it.

If the stop watch is started again without resetting it, the start time is the current displayed time (not zero).

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| Note Symbol assignment is not case sensitive. If you want to access all elements of a panel the notation "" is used, see example below. |  |
| Example "Signal:SleepInd""Signal:easy/MotorState/EngineSpeed""SysVar:SysVarTester" (for a system variable defined with name space TestSysvar in the configuration) |  |

## Return Values

—

## Example

```c
// Stop the clock control designed as stop watch.
on key 'a'
{
ClockControlStop("ClockControl", "StoppWatch");
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
