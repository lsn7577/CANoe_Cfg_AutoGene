# ChkStart_SignalCycleTimeViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_SignalCycleTimeViolation (Signal ObservedSignal, duration MinCycleTime, duration MaxCycleTime);
dword ChkStart_SignalCycleTimeViolation (Signal ObservedSignal, duration MinCycleTime, duration MaxCycleTime, char[] CaplCallback);
```

## Description

Checks the occurrences of a signal.

An event will be generated, if the time between two consecutive signal occurrences is out of the specified range.

## Parameters

| Name | Description |
|---|---|
| ObservedSignal | Signal to observe. It must exist in DB |
| 0 | Minimum cycle time shall not be checked |
| > 0 | Minimum allowed cycle time |
| 0 | Maximum cycle time shall not be checked |
| > 0 | Maximum allowed cycle time |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Return Values

CheckId [dword]

## Example

```c
...
dword checkId;
// Create and start the check for LIN wake-up request
checkId = ChkStart_SignalCycleTimeViolation(Motor1State_Cycl::Motor1Temp,
            29,   // min. cycle time in ms
            32,   // max cycle time in ms
            "SigCycleTimeCallback"); 
...
// CAPL callback for violation notification
void SigCycleTimeCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | LIN CAN (since 7.5) A429 (since 8.5 SP4) | LIN CAN A429 | — | LIN CAN A429 | LIN CAN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
