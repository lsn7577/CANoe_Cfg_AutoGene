# TestWaitForRawSignalMatch

> Category: `Test` | Type: `function`

## Syntax

```c
TestWaitForRawSignalMatch(dbSignal aSignal, int64 value, dword aTimeout); // form 1
TestWaitForRawSignalMatch(char aSignalName[], int64 value, dword aTimeout); // form 2
TestWaitForRawSignalMatch(dbSignal aSignal, byte data[], dword dataLength, dword aTimeout); // form 3
TestWaitForRawSignalMatch(char aSignalName[], byte data[], dword dataLength, doword aTimeout); // form 4
```

## Description

Checks the given raw value against the value of the signal. The resolution of the signal is considered.

If this condition is already met when this function is called, it returns immediately without waiting.

The test step is evaluated as either passed or failed depending on the results.

## Parameters

| Name | Description |
|---|---|
| Note The int64 parameter is interpreted as qword and will be casted according to the signal type. If a byte comparison is required, an byte array should be used. |  |

## Example

```c
// waits for a specified value of signal ‘Velocity’
long result;
result = TestWaitForRawSignalMatch(Node_SUT::Velocity, 80, 1000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
