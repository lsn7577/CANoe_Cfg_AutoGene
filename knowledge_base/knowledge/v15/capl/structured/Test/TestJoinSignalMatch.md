# TestJoinSignalMatch

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinSignalMatch (Signal aSignal, float CompareValue); // form 1
long TestJoinSignalMatch (dbEnvVar aEnvVar, float CompareValue); // form 2
long TestJoinSignalMatch (sysvar aSysVar, float CompareValue); // form 3
long TestJoinSignalMatch (Signal aSignal, float CompareValue, word waitForSignalUpdate); // form 4
long TestJoinSignalMatch (sysvar aSysVar, int64 CompareValue); // form 5
long TestJoinSignalMatch (ServiceSignalNumber aSignal, float CompareValue); // form 6
long TestJoinSignalMatch (ServiceSignalNumber aSignal, float CompareValue, word waitForSignalUpdate); // form 7
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

By default this condition will be checked immediately when the set of joined events is evaluated by TestWaitForAllJoinedEvents or TestWaitForAnyJoinedEvent and may not wait for a value change. It is also possible to delay the checking of the condition until the next message with the given signal arrives.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

```c
// waits until signal ‘Velocity’ matches to a specific value
long result;
dword index = 0;
result = TestJoinSignalMatch(Node_SUT::Velocity, 80);
// ... other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinTextEvent("ErrorFrame occurred!");

index = TestWaitForAllJoinedEvents(500);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2: form 1 7.5: form 2, 3 8.5 SP3: form 4, 5 9.0 SP4: form 6, 7 | 13.0 | — | 14 | 1.0: form 1-3 2.0 SP2: form 4, 5 2.1 SP4: form 6, 7 |
| Restricted To | — | — | — | — | form 3, 5 | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
