# TestValidateSignalMatch

> Category: `Test` | Type: `function`

## Syntax

```c
long TestValidateSignalMatch (char aTestStep[], Signal aSignal, float aCompareValue); // form 1
long TestValidateSignalMatch (char aTestStep[], dbEnvVar aEnvVar, float aCompareValue); // form 2
long TestValidateSignalMatch (char aTestStep[], sysvar aSysVar, float aCompareValue); // form 3
long TestValidateSignalMatch (char aTestStep[], sysvar aSysVar, int64 aCompareValue); // form 4
long TestValidateSignalMatch (char aTestStep[], ServiceSignalNumber aSignal, float aCompareValue); // form 5
```

## Description

Checks the given value against the value of the signal, the system variable or the environment variable. The resolution of the signal is considered.

The test step is evaluated as either passed or failed depending on the results.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

```c
// validates the value of the signal against the given value
long result;
result = TestValidateSignalMatch("Check Velocity", Node_SUT::Velocity, 80);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2: form 1 7.5: form 2, 3 8.5 SP3: form 4 9.0 SP4: form 5 | 13.0 | — | 14 | 1.0: form 1-3 2.0 SP2: form 4 2.1 SP4: form 5 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
