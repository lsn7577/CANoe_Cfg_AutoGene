# coTfsSetFailControl

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetFailControl( dword controlValue );
```

## Description

Determines the behavior of CANopen test feature set tests. The entries in the test report can be switched with this function, that is, a test that in the default setting 0 has passed also receives the note "passed" in the test protocol. Conversely, a failed test receives the note "failed".

The call of this function with the parameter 1 reverses the behavior. If the device should pass a test, failed is in the test report and vice-versa. This behavior can be used to create a negative test.

After measurement start, the setting 0 is always active.

The return value of the test functions themselves in the CAPL program is never changed, only the protocol is adjusted.

## Parameters

| Name | Description |
|---|---|
| controlValue | 0: normal behavior (default) 1: inverted behavior 2: the test case is not marked with pass or fail in the test report, the user must ensure the corresponding entries himself |

## Return Values

Error code

## Example

```c
coTfsSetFailControl (1); // invert report behavior

// run some negative tests

coTfsSetFailControl (0); // switch back to normal behavior
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
