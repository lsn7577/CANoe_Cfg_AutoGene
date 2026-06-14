# TestWaitForUpdateFlag

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForUpdateFlag(valueHandle * value, dword timeoutMs);
```

## Description

Waits for the update flag of a valueHandle to be set. Each valueHandle has an update flag which is set when the value is updated and reset through an explicit call to valueHandle::ClearUpdateFlag or valueHandle::ResetValueState.

Use this function instead of TestWaitForUpdate if an undetermined number of updates may occur between a point where you reset the flag and a point where at least one update must have occurred.

## Parameters

| Name | Description |
|---|---|
| value | Value handle of a communication object or distributed object. |
| timeoutMS | Timeout in milliseconds. |

## Example

```c
long ret;
consumedEventRef * anEvent;
anEvent = lookupConsumedEvent(path);
anEvent.ClearUpdateFlag();
// ...
ret = testWaitForUpdateFlag(anEvent, 200);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
