# TestJoinTextEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinTextEvent(char[]aText)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Parameters

| Name | Description |
|---|---|
| aText | Textual event that should be awaited |

## Example

```c
// waits for a specified text event
long result;
dword index = 0;
result = TestJoinTextEvent("ErrorFrame occurred!");
// ... other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinSignalInRange(Velocity, 80, 100);

index = TestWaitForAnyJoinedEvent(2000);

// on ErrorFrame handler
on errorFrame
{
   TestSupplyTextEvent("ErrorFrame occurred!");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
