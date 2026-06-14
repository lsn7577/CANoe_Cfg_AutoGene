# ChkStart_LINETFViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINETFViolation (dword ETFFrameId, char[] CaplCallback);
dword ChkStart_LINETFViolation (dword ETFFrameId);
```

## Description

Checks the format of a single response to ETF. An event will be generated, if the first data byte does not match protected ID of any of the associated frames (Slave failure).

Checks the collision resolution process. An event will be generated during collision resolution, if one of the following is detected:

## Parameters

| Name | Description |
|---|---|
| ETFFrameId | Frame identifier (8 bits) of an event triggered frame to verify |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Example

```c
...
dword checkId;
// Create and start the check for LIN Event-triggered frame
// Parameters: Frame identifier of event-triggered frame to verify and optional CAPL 
// callback
checkId = ChkStart_LINETFViolation (0x3A, "CallbackLINETFViolation"); 
...
// CAPL callback for violation notification
void CallbackLINETFViolation (dword aCheckId)
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
