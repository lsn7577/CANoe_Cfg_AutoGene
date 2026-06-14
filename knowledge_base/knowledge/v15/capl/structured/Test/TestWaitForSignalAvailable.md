# TestWaitForSignalAvailable

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSignalAvailable (Signal aSignal, dword aTimeout); // form 1
long TestWaitForSignalAvailable (ServiceSignal aSignal, dword aTimeout); // form 2
```

## Description

Tests the availability of a specific signal and waits if necessary until its availability. A signal that is received at least once from the bus after the measurement starts is classified as "available".

This function is useful when you want to assure that single signals are available before starting a signal-oriented test, i.e. to synchronize the tester with the bus.

## Parameters

| Name | Description |
|---|---|
| aSignal | Signal whose availability is being tested or for which is waited |
| aTimeout | Maximum waiting time in ms. |

## Example

```c
// waits for the occurrence of signal ‚EngineRunning’
long result;
result = TestWaitForSignalAvailable(EngineRunning, 2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP3: form 1 10.0: form 2 | 13.0 | — | — | 1.0: form 1 2.2: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
