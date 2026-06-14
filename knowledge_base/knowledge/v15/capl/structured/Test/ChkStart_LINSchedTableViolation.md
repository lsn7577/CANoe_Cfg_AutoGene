# ChkStart_LINSchedTableViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINSchedTableViolation (dword TableIndex, duration Jitter);
dword ChkStart_LINSchedTableViolation (dword TableIndex);
dword ChkStart_LINSchedTableViolation (dword TableIndex, duration Jitter, char[] CaplCallback);
dword ChkStart_LINSchedTableViolation (dword TableIndex, char[] CaplCallback);
```

## Description

Checks a certain LIN schedule table for correspondence with the database definition.

An event will be generated, if

## Parameters

| Name | Description |
|---|---|
| TableIndex | Zero based index of schedule table to be checked. |
| Jitter | Allowed deviation from the timing defined by schedule tables. For this value usually Master’s Jitter is used. Measured slot delay should be in the range: D - Jitter <= M <= D + Jitter; where M is measured delay and D is expected delay. Unit: Can be set with ChkConfig_SetPrecision.Default: Master’s Jitter defined in LDF. |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(6); // switch to µs precision
// Create and start the check for LIN schedule table with index 0
checkId = ChkStart_LINSchedTableViolation(0, "LINSchedTableCallback"); 
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINSchedTableCallback (dword aCheckId)
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
