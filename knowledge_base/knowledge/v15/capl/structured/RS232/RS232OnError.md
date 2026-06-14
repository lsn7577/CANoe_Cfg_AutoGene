# RS232OnError

> Category: `RS232` | Type: `function`

## Syntax

```c
RS232OnError( dword port, dword errorFlags );
```

## Description

Callback handler for reception of errors at a serial port.

## Parameters

| Name | Description |
|---|---|
| port | A number between 1 and 255 identifying a serial port. |
| Bit | Error |
| 0 | Send operation failed. |
| 1 | Receive operation failed. |
| 2 | Frame error. May be caused by parity mismatch or any other frame mismatch (e.g. number of stop bits). |
| 3 | Frame parity error. Is caused by parity mismatch. |
| 4 | Buffer overrun. It is not specified if the driver of the sender cannot send fast enough, if it is up to the receiver which got too much data in too short time or anything else. |
| 5 | Buffer overrun at receiver. |
| 6 | Break state. Other end requested to pause. |
| 7 | Timeout. May be caused by wrongly set too short timeout. See RS232SetHandshake for setting the timeout. |
| Note Several error bits may be set at the same time. Some error flags are up to the driver manufacturer what they mean and when they are issued. |  |

## Return Values

—

## Example

```c
RS232OnError(dword port, dword errorFlags)
{
   if ( errorFlags & 1 )
      writeLineEx(0,3,“send failed”);
   if ( errorFlags & 2 )
      writeLineEx(0,3,“receive failed”);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 | 7.1 | — | — | 14 | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | — | — | ✔ | N/A |
