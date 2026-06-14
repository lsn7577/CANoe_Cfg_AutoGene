# SCC_SetVerbosity

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SetVerbosity ( dword Level )
```

## Description

Sets the Verbosity parameter of the DLL. The higher the value is, the more information will be output in the write window.

## Parameters

| Name | Description |
|---|---|
| Selector | Description of return value |
| 0 | Signals only critical errors. |
| 1 | Signals errors due to erroneous configurations, etc. |
| 2 | Warns, if an unexpected protocol status is reached, and signals missing obligatory callbacks. |
| 3 | Informs about missing optional callbacks and minor problems. |
| >3 | Signals low level events such as setting and expiring of timers. |

## Return Values

—

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
