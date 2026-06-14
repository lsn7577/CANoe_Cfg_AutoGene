# TestJoinSignalInRange

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinSignalInRange (Signal aSignal, float aLowLimit, float aHighLimit); // form 1
long TestJoinSignalInRange (dbEnvVar aEnvVar, float aLowLimit, float aHighLimit); // form 2
long TestJoinSignalInRange (sysvar aSysVar, float aLowLimit, float aHighLimit); // form 3
long TestJoinSignalInRange (Signal aSignal, float aLowLimit, float aHighLimit, word waitForSignalUpdate); // form 4
long TestJoinSignalInRange (sysvar aSysVar, int64 aLowLimit, int64 aHighLimit); // form 5
long TestJoinSignalInRange (ServiceSignalNumber aSignal, float aLowLimit, float aHighLimit); // form 6
long TestJoinSignalInRange (ServiceSignalNumber aSignal, float aLowLimit, float aHighLimit, word waitForSignalUpdate); // form 7
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
// waits until the value of signal ‚Velocity’ is in the given range
long result;
dword index = 0;
result = TestJoinSignalInRange(Velocity, 30, 50);
// ... other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinTextEvent("ErrorFrame occurred!");

index = TestWaitForAnyJoinedEvent(2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP3: form 1-3 8.5 SP3: form 4, 5 9.0 SP4: form 6, 7 | 13.0 | — | — | 1.0: form 1-3 2.0 SP2: form 4, 5 2.1 SP4: form 6, 7 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
