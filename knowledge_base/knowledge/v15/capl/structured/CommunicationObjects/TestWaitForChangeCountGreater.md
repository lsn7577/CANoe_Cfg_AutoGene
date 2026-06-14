# TestWaitForChangeCountGreater

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForChangeCountGreater(valueHandle * value, qword count, dword timeoutMs);
```

## Description

Waits for the change counter of a valueHandle to reach a certain value. Each valueHandle contains a change counter which is reset to 0 at measurement start and with explicit calls to valueHandle::ResetValueState. You can read out the counter with valueHandle::GetChangeCount.

## Parameters

| Name | Description |
|---|---|
| value | Value handle of a communication object or distributed object. |
| count | Change count to be reached. |
| timeoutMS | Timeout in milliseconds. |

## Example

```c
long ret;
consumedEventRef * anEvent;
anEvent = lookupConsumedEvent(path);
// ...
ret = testWaitForChangeCountGreater(anEvent, anEvent.GetChangeCount() + 3, 200);
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
