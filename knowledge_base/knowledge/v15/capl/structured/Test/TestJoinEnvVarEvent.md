# TestJoinEnvVarEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinEnvVarEvent(dbEnvVar aEnvVar)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aEnvVar | Environment variable that should be awaited. |

## Example

Example 1

```c
putValue (evMyEnvVar, 1);
TestJoinEnvVarEvent (evMyEnvVar);
TestWaitForAnyJoinedEvent (1000); // Does not wait, is immediately discontinued by an environment variable change!
// add envVar event to the current set of “joined events” and get the envVar value
dword index = 0;
float evValue = 0;
TestJoinEnvVarEvent(MyEnvVar);
// ... other join events
TestJoinSignalInRange(Velocity, 80, 100);
TestJoinTextEvent("ErrorFrame occurred!");

index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventEnvVarData(index, evValue);
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
