# TestResetEnvVarValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetEnvVarValue (dbEnvVar aEnvVar);
```

## Description

Resets the environment variable to initial value. If no initial value is available, the environment variable is set to 0 or "".

## Parameters

| Name | Description |
|---|---|
| aEnvVar | Environment variable that should be reset. |

## Example

```c
// check reaction of signal “LockState” after crash
@EnvErrorCrashDetected = 1;
TestWaitForTimeout(100);
if ($LockState !=  Unlocked)
    TestStepFail(“Doors are locked after crash is detected!”);

// reset the crash environment variable
TestResetEnvVarValue(EnvErrorCrashDetected);
TestWaitForTimeout(200);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
