# ChkStart_LINWakeupReqLengthViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINWakeupReqLengthViolation (duration MinLength, duration MaxLength);
dword ChkStart_LINWakeupReqLengthViolation (duration MinLength, duration MaxLength, char[] CaplCallback);
```

## Description

Checks the length of LIN wake-up request.

An event will be generated, if a measured length of the wake-up request is out of the specified range.

## Parameters

| Name | Description |
|---|---|
| 0 | Minimum length shall not be checked |
| >0 | Minimum allowed length |
| 0 | Maximum length shall not be checked |
| >0 | Maximum allowed length time |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Return Values

CheckId [dword]

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(6); // switch to µs precision
// Create and start the check for LIN wake-up request
checkId = ChkStart_LINWakeupReqLengthViolation(250, 1000, "LINWakeupLenCallback");
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINWakeupLenCallback (dword aCheckId)
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
