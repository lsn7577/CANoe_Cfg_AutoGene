# TestWaitForSignalOutsideRange

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSignalOutsideRange (sysvar aSysVar, float aLowLimit, float aHighLimit, dword aTimeout); // form 1
long TestWaitForSignalOutsideRange (dbEnvVar aEnvVar, float aLowLimit, float aHighLimit, dword aTimeout); // form 2
long TestWaitForSignalOutsideRange (Signal aSignal, float aLowLimit, float aHighLimit, dword aTimeout); // form 3
long TestWaitForSignalOutsideRange (sysvar aSysVar, int64 aLowLimit, int64 aHighLimit, dword aTimeout); // form 4
long TestWaitForSignalOutsideRange (ServiceSignalNumber aSignal, float aLowLimit, float aHighLimit, dword aTimeout); // form 5
```

## Description

Checks the signal, the system or the environment variable value against the condition:

If this condition is already met when this function is called, it returns immediately without waiting.

The test step is evaluated as passed or failed depending on the results.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

```c
// waits for a specified value range of signal ‘Velocity’
long result;
result = TestWaitForSignalOutsideRange(Velocity, 80, 100, 2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0: form 1 7.1 SP3: form 3 8.5 SP3: form 4 9.0 SP4: form 5 | 13.0 | — | 14 | 1.0: form 1-3 2.0 SP2: form 4 2.1 SP4: form 5 |
| Restricted To | — | — | — | — | form 1, 4 | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
