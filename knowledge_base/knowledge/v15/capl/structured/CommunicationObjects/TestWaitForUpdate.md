# TestWaitForUpdate

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForUpdate(valueHandle * value, dword timeoutMs);
```

## Description

Waits for the next update of a valueHandle. This is equivalent to calling TestWaitForUpdateCountGreater (value, value.GetUpdateCount(), timeoutMs).

Note that only updates which occur while the function waits are considered. If you want to wait for updates which may occur earlier, or if you want to wait for several updates, use TestWaitForUpdateFlag or TestWaitForUpdateCountGreater.

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
// ...
ret = testWaitForUpdate(anEvent, 200);
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
