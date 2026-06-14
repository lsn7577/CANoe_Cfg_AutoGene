# TestJoinDiagResponseFromEcu

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinDiagResponseFromEcu()
long TestJoinDiagResponseFromEcu( char ecuQualifier[])
```

## Description

Adds an event of type diagnostic response reception to the set of joined events. This is a non-blocking function.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | If given, only a response from the indicated ECU will fire the event. |

## Return Values

Number of conditions in stock:
Error code

## Example

```c
// waits for a diagnostic response
// wait is resumed on check event
dword index = 0;

TestJoinDiagResponseFromEcu();
// … other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinSignalInRange(Velocity, 80, 100);
TestJoinTextEvent("ErrorFrame occurred!");

Index = TestWaitForAnyJoinedEvent(2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP3 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
