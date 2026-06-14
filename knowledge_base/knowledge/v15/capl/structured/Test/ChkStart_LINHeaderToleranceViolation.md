# ChkStart_LINHeaderToleranceViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINHeaderToleranceViolation (float Tolerance);
dword ChkStart_LINHeaderToleranceViolation (float Tolerance, char[] CaplCallback);
```

## Description

Checks the LIN header transmission time.

An event will be generated, if the measured header transmission time is over specified tolerance.

## Parameters

| Name | Description |
|---|---|
| Tolerance | Allowed tolerance for Header transmission time. Value range: [0 .. 40]Unit: percents [%] |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Example

```c
...
dword checkId;
// Create and start the check for LIN Header tolerance
checkId = ChkStart_LINHeaderToleranceViolation(40.0, "LINHeaderToleranceCallback");
...
// CAPL callback for violation notification
void LINHeaderToleranceCallback (dword aCheckId)
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
