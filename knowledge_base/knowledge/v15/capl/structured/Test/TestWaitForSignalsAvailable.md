# TestWaitForSignalsAvailable

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSignalsAvailable (dbNode aNode, dword aTimeout);
```

## Description

Tests the availability of all the send signals of a node and waits if necessary until all the send signals of the node are available. Signals that are received at least once from the bus after the measurement starts are classified as "available".

This function is useful when you want to assure that all signals are available before starting a signal-oriented test, i.e. to synchronize the tester with the bus.

## Parameters

| Name | Description |
|---|---|
| aNode | Node whose send signals should all be available For CAN and FlexRay all signals are considered! In contrast to the corresponding XML pattern <awaitsignalsavailable> this function considers FlexRay signals from all frames and PDUs; not only FlexRay signals from frames and PDUs of service type 'Application'. For LIN nodes only signals from unconditional and event-triggered frames of all schedule tables are considered. Also the signals of diagnostic frames are ignored. Functional for LIN since CANoe 8.1 SP2. In previous versions the function did not work for LIN and returned -1. |
| aTimeout [ms] | Maximum waiting time |

## Example

```c
// waits for the availability of all tx signals of node ‘SUT’
long result;
result = TestWaitForSignalsAvailable(SUT, 2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP3 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
