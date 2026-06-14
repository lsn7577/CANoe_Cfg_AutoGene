# ChkStart_LINWakeupRetryViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINWakeupRetryViolation (duration TimeoutAfterWakeup, duration TimeoutAfterThreeWakeups, float Tolerance, dword MaxRetryNum, char[] CaplCallback);
dword ChkStart_LINWakeupRetryViolation (duration TimeoutAfterWakeup, duration TimeoutAfterThreeWakeups, float Tolerance, dword MaxRetryNum);
dword ChkStart_LINWakeupRetryViolation (dword MaxRetryNum, char[] CaplCallback);
dword ChkStart_LINWakeupRetryViolation (dword MaxRetryNum);
```

## Description

Checks number of LIN wake-up signals and the time between them.

An event will be generated, if

## Parameters

| Name | Description |
|---|---|
| 0 | Timeout between two consecutive retransmissions shall not be checked |
| > 0 | Timeout between two consecutive retransmissions |
| 0 | Timeout after each three retransmissions shall not be checked |
| > 0 | Timeout after each three retransmissions |
| Tolerance | Allowed tolerance for timeout values Value range: [0 .. 100] Unit: percents [%] Default: 14%. |
| 0 | Maximum number of retransmissions shall not be checked |
| > 0 | Maximum allowed number of retransmissions |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(3); // set precision to ms
// Create and start the check for LIN Wake-Up signals
// Parameters to validate: Timeout between two wake-up signals – 150 ms,
// Timeout after each three wake-up signals – 1.5 sec, Allowed tolerance 2%, maximum 
// expected number of retransmitted Wake-Up signals - 4
checkId = ChkStart_LINWakeupRetryViolation (150, 1500, 2, 4, " LINWakeupRetryCallback"); 
...
// CAPL callback for violation notification
void LINWakeupRetryCallback (dword aCheckId)
{
ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | LIN | LIN | — | LIN | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
