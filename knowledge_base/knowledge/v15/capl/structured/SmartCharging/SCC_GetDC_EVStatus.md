# SCC_GetDC_EVStatus

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetDC_EVStatus ( long& EVReady, long& EVCabinConditioning, long& EVRESSConditioning, char EVErrorCode[], long& EVRESSSOC) // form 1
void SCC_GetDC_EVStatus ( long& EVReady, char EVErrorCode[], long& EVRESSSOC) // form 2
```

## Description

Gets the elements of DC_EVStatus (DIN/ISO) of a received DC message.

## Return Values

Returns the DC status bits of the vehicle and its error code, if contained in the message.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
