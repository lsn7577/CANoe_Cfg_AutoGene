# ChkStart_LINSyncDelTimingViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINSyncDelTimingViolation (float MinDelLen, float MaxDelLen);
dword ChkStart_LINSyncDelTimingViolation (float MinDelLen, float MaxDelLen, char[] CaplCallback);
```

## Description

Checks the timing of the synchronization break field in LIN headers.

An event will be generated, if the measured length [in bit times] of break delimiter is outside of the specified range.

## Parameters

| Name | Description |
|---|---|
| 0 | Minimum length of break delimiter shall not be checked |
| >0 | Minimum allowed length of break delimiter |
| 0 | Maximum length of break delimiter shall not be checked |
| >0 | Maximum allowed length of break delimiter |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(9); // switch to ns precision
// Create and start the check for LIN Synch Delimiter violation
checkId = ChkStart_LINSyncDelTimingViolation(1, 5, "LINSyncDelimiterCallback"); 
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINSyncDelimiterCallback (dword aCheckId)
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
