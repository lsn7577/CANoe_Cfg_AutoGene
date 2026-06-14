# TestJoinMessageEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinMessageEvent (dbMsg aMessage)
long TestJoinMessageEvent (dword aMessageId)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message that should be awaited. |
| aMessageId | Numeric ID of the message for which should be waited. |

## Example

```c
// add msg event to the current set of “joined events” and fill the msg data to message ‘eventMessage’
dword index = 0;
TestJoinMessageEvent(VehicleMotion);
// ... other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinSignalInRange(Velocity, 80, 100);
TestJoinTextEvent("ErrorFrame occurred!");

index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventMsgData(index, eventMessage);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
