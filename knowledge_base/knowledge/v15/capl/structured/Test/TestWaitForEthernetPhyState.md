# TestWaitForEthernetPhyState

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForEthernetPhyState(ethernetport hwport, long state, dword aTimeout);
```

## Description

Waits for the occurrence of the specified Ethernet PHY state. Should the Ethernet PHY state not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless. If the Ethernet PHY has already the expected state, the function returns immediately with return value 1.

## Parameters

| Name | Description |
|---|---|
| hwPort | Hardware port qualifier. |
| state | Wait for this state: 1: normal state 2: sleep state 3: power off state 4: sleep request |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 | 15 | — | — | 6 |
| Restricted To | — | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
