# ChkStart_LINDiagDelayTimesViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINDiagDelayTimesViolation (Node ObservedNode);
dword ChkStart_LINDiagDelayTimesViolation ();
dword ChkStart_LINDiagDelayTimesViolation(Node ObservedNode, char[] CaplCallback);
dword ChkStart_ LINDiagDelayTimesViolation(char[] CaplCallback);
```

## Description

Checks the values of P2_min and ST_min for a specified LIN Slave node or for all LIN Slaves defined in LDF.

An event will be generated, if the measured P2_min or ST_min value is smaller than one specified in the database (LDF).

## Parameters

| Name | Description |
|---|---|
| ObservedNode | Slave node to be checked. |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Example

```c
...
dword checkId;
// Create and start the check for LIN diagnostic delay times
checkId = ChkStart_LINDiagDelayTimesViolation("LINDiagDelayTimesCallback"); 
...
// CAPL callback for violation notification
void LINDiagDelayTimesCallback (dword aCheckId)
{   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | — | — | — | 1.0 |
| Restricted To | — | LIN | — | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
