# TestWaitForValueSInt

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForValueSInt(valueHandle * value, int64 awaitedValue, dword timeoutMs);
```

## Description

Waits for a valueHandle to reach a certain value. This function can only be used for valueHandles with a signed integer data type. It cannot be used for system variables or bus system signals.

## Parameters

| Name | Description |
|---|---|
| value | Value handle of a communication object or distributed object. |
| awaitedValue | Value which is awaited. |
| timeoutMS | Timeout in milliseconds. |

## Example

```c
long ret;
ret = testWaitForValueSInt(ErrorSignal[LeftMirror], -1, 200);
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
