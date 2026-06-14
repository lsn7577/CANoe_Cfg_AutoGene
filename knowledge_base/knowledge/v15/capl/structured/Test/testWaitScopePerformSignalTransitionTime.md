# testWaitScopePerformSignalTransitionTime

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopePerformSignalTransitionTime (message aMessage, ScopeAnalyseRange range, dword flags, long thresholdStart, long thresholdEnd, ScopeBitTransitionTimeResult result, ScopeAnalyseHandle handle); // form 1
long testWaitScopePerformSignalTransitionTime (char nodeName[],ScopeAnalyseRange range, dword flags, long thresholdStart, long thresholdEnd, ScopeBitTransitionTimeResult result, ScopeAnalyseHandle handle); // form 2
long testWaitScopePerformSignalTransitionTime (linFrame aMessage, ScopeAnalyseRange range, dword flags, long thresholdStart, long thresholdEnd, ScopeBitTransitionTimeResult result, ScopeAnalyseHandle handle); // form 3
long testWaitScopePerformSignalTransitionTime (frFrame aMessage, ScopeAnalyseRange range, dword flags, long thresholdStart, long thresholdEnd, ScopeBitTransitionTimeResult result, ScopeAnalyseHandle handle); // form 4
```

## Description

Form 1: Measures the transition time of rising and falling edges of a CAN message within the defined area.

Form 2: Measures the transition time of rising and falling edges of all Tx messages of an ECU node within the defined area.

Form 3: Measures the transition time of rising and falling edges of a LIN message within the defined area.

Form 4: Measures the transition time of rising and falling edges of a FlexRay message within the defined area.

## Parameters

| Name | Type | Description |
|---|---|---|
| aMessage |  | The message to be analyzed. |
| nodeName |  | The ECU node name of a database node. |
| range |  | The start and end of the transition time measurement. See Class: scopeAnalyseRange. |
| Bits |  | Description |
| 0 |  | Define threshold level unit:0 = Threshold level in mV1 = Threshold level in % |
| 1-3 |  | Select signal for transition time measurementOnly one of the three bits must be set (only valid for CAN)Bit 1 = 1 Use CANhigh Bit 2 = 1 Use CANLow Bit 3 = 1 Use CANdiff |
| 4-5 |  | Rising/falling edge selection Bit 4 = 1 Use rising edgesBit 5 = 1 Use falling edges |
| 6 |  | 0 = Use last occurrence for transition time measurement, where the voltage level is above or below the threshold level. 1 = Use first occurrence for transition time measurement, where the voltage level is above or below the threshold level. All other bits are reserved and must be set to 0. |
| Keyword | Description | Type |
| minValue | The minimal transition time | float |
| maxValue | The maximal transition time | float |
| averageValue | The average transition time overall measured edges | float |
| stdDeviation | The standard deviation of the transition time measurement | float |
| scopeSamplingPeriod | The configured sample period of the scope device | float |
| countAnalyzedEdges | The count of analyzed edges | long |
| countAnalyzedFrames | The count of analyzed frames | long |
| Keyword | Description | Type |
| handle | A unique ID | long |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0: form 1-3 11.0: form 4 | 13.0 | — | — | 3.0: form 1-3 3.0: form 4 |
| Restricted To | — | CAN (form 1-3) LIN (form 1-3) FlexRay (form 1-4) Scope (form 1-4) | CAN (form 1-3) LIN (form 1-3) FlexRay (form 1-4) Scope (form 1-4) | — | — | CAN (form 1-3) LIN (form 1-3) FlexRay (form 1-4) Scope (form 1-4) |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
