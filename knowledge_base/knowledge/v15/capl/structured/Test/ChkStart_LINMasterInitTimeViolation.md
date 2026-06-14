# ChkStart_LINMasterInitTimeViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINMasterInitTimeViolation (duration MinTime, duration MaxTime);
dword ChkStart_LINMasterInitTimeViolation (duration MinTime, duration MaxTime, char[] CaplCallback);
```

## Description

Checks an initialization time of LIN Master. The initialization state is entered on switching on and on waking up.

An event will be generated, if the initialization time is out of the specified range.

## Parameters

| Name | Description |
|---|---|
| 0 | Minimum time shall not be checked |
| >0 | Minimum allowed initialization time |
| 0 | Maximum time shall not be checked |
| >0 | Maximum allowed initialization time |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Example

```c
...
dword checkId;
// Create and start the check for LIN Master initialization time violation
checkId = ChkStart_LINMasterInitTimeViolation(100, 150, "LINMasterInitTimeCallback"); 
...
// CAPL callback for violation notification
void LINMasterInitTimeViolation (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | LIN | LIN | — | LIN | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
