# TestWaitForEnvVar

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForEnvVar(dbEnvVar aEnvVar, dword aTimeout); // form 1
long TestWaitForEnvVar(char aEnvVarName[], dword aTimeout); // form 2
```

## Description

Waits for the description of the specified environment variable (aEnvVar or with the name aEnvVarName). Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aEnvVar | Environment variable that should be awaited |
| aEnvVarName | Name of environment variable that should be awaited |
| aTimeout | Maximum time that should be waited [ms](Transmission of 0: no timeout controlling) |

## Example

```c
// waiting point is discontinued immediately
long result;
putValue (evMyEnvVar, 1);
result = TestWaitForEnvVar (evMyEnvVar, 1000); // Does not wait, is immediately discontinued by an environment variable change!
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0: form 1 7.5: form 2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
