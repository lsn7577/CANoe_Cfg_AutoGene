# ChkStart_LINRespErrorSignal

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINRespErrorSignal (Node ObservedNode);
dword ChkStart_LINRespErrorSignal ();
dword ChkStart_LINRespErrorSignal ( Node ObservedNode, char[] CaplCallback);
dword ChkStart_LINRespErrorSignal (char[] CaplCallback);
```

## Description

Checks the LIN Response_Error signal for a specified LIN Slave node or for all LIN nodes.

An event will be generated, if the Response_Error signal value changes from FALSE (0) to TRUE (1).

J2602 specific: Bit 7 of Status Byte serves as Response_Error signal.

## Parameters

| Name | Description |
|---|---|
| ObservedNode | Node to be checked.Only Slave nodes are allowed. |
| CaplCallback | Name of CAPL callback function to be called on generated event. In simulation nodes this parameter has to be set. In test modules this parameter is optional. |

## Example

```c
...
dword checkId;
// Create and start the check for LIN response_error signal
checkId = ChkStart_LINRespErrorSignal("LINRespErrCallback"); 
...
// CAPL callback for violation notification
void LINRespErrCallback (dword aCheckId)
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
