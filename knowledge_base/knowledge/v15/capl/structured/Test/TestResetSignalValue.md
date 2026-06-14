# TestResetSignalValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetSignalValue (Signal aSignal); // form 1
long TestResetSignalValue (ServiceSignal aSignal); // form 2
```

## Description

Resets the signal to initial value. The sending depends on the message send typ.

The reset-function does not contain a waiting time which guarantees that the signal is sent out on the bus. If a waiting time is desired, the TestWaitForTimeout function has additionally been executed.

## Parameters

| Name | Description |
|---|---|
| aSignal | Signal that should be reset. |

## Example

```c
// check reaction of signal “LockState” after crash
$CrashDetected = 1;
TestWaitForTimeout(100);
if ($LockState !=  Unlocked)
    TestStepFail(“Doors are locked after crash is detected!”);

// reset test signals
TestResetSignalValue(CrashDetected);
TestResetSignalValue(LockState);
TestWaitForTimeout(200);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5: from 1 9.0 SP4: form 2 | 13.0 | — | — | 1.0: form 1 2.1 SP4: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
