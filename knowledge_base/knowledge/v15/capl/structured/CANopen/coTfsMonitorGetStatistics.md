# coTfsMonitorGetStatistics

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsMonitorGetStatistics( dword nodeId, dword requestType, dword minValue[1], dword maxValue[1], dword averageValue[1], dword passedCounter[1] , dword failedCounter[1]);
```

## Description

This function returns the statistics information that are monitored between coTfsMonitorActivate and coTfsMonitorDeactivate.

## Parameters

| Name | Description |
|---|---|
| nodeId | Node-ID [1..127] |
| requestType | Values to be monitored. 1 - SDO time values2 - NMT time values3 - LSS time values |
| minValue[1] | Minimum value in [ms]. |
| maxValue[1] | Maximum value in [ms]. |
| averageValue[1] | Average value in [ms]. |
| passedCounter[1] | Number of values within the allowed range. |
| failedCounter[1] | Number of values out of the allowed range. |

## Return Values

Error code

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
