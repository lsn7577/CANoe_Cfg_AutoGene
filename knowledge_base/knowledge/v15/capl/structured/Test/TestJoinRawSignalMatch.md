# TestJoinRawSignalMatch

> Category: `Test` | Type: `function`

## Syntax

```c
TestJoinRawSignalMatch(dbSignal aSignal, int64 value); // form 1
TestJoinRawSignalMatch(char aSignalName[], int64 value); // form 2
TestJoinRawSignalMatch(dbSignal aSignal, byte data[], dword dataLength); // form 3
TestJoinRawSignalMatch(char aSignalName[], byte data[], dword dataLength); // form 4
```

## Description

Completes the current set of joined events with the transmitted event. This function does not wait.

By default this condition will be checked immediately when the set of joined events is evaluated by TestWaitForAllJoinedEvents or TestWaitForAnyJoinedEvent and may not wait for a value change. It is also possible to delay the checking of the condition until the next message with the given signal arrives.

## Parameters

| Name | Description |
|---|---|
| Note The int64 parameter is interpreted as qword and will be casted according to the signal type. If a byte comparison is required, an byte array should be used. |  |

## Example

```c
// waits until signal ‘Velocity’ matches to a specific value
long result;
dword index = 0;
result = TestJoinRawSignalMatch(Node_SUT::Velocity, 0.8);
// ... other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinTextEvent("ErrorFrame occurred!");

index = TestWaitForAllJoinedEvents(500);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
