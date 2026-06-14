# checkSignalInRange

> Category: `Test` | Type: `function`

## Syntax

```c
long checkSignalInRange(Signal aSignal, float aLowLimit, float aHighLimit); // form 1
long checkSignalInRange(EnvVarName, float aLowLimit, float aHighLimit); // form 2
long checkSignalInRange(sysVar aSysVar, float aLowLimit, float aHighLimit); // form 3
long checkSignalInRange(sysVar aSysVar, int64 aLowLimit, int64 aHighLimit); // form 4
long checkSignalInRange(ServiceSignalNumber aSignal, float aLowLimit, float aHighLimit); // form 5
```

## Description

Checks the signal value or the environment variable value or the system variable value against the condition:

aLowLimit <= Value <= aHighLimit

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

```c
// checks if the value of the signal is in the given range
long result;
result = checkSignalInRange(Node_SUT::Velocity, 60, 100);
if (result != 1)
TestStepFail("Value of signal is not in the allowed range!");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1: form 1 6.0: form 2 7.0: form 3 8.5 SP3: form 4 9.0 SP4: form 5 | 13.0 | — | 14 | 1.0: form 1-3 2.0 SP2: form 4 2.1 SP4: form 5 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
