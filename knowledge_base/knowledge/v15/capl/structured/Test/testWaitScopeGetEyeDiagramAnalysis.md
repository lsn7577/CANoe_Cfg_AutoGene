# testWaitScopeGetEyeDiagramAnalysis

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetEyeDiagramAnalysis(ScopeAnalyseHandle handle, message frame, long errorNo, ScopeSerialBitAnalysisViolationData data); // form 1
long testWaitScopeGetEyeDiagramAnalysis(ScopeAnalyseHandle handle, linFrame frame, long errorNo, ScopeSerialBitAnalysisViolationData data); // form 2
long testWaitScopeGetEyeDiagramAnalysis(ScopeAnalyseHandle handle, frFrame frame, long errorNo, ScopeSerialBitAnalysisViolationData data); // form 3
```

## Description

Returns the violation data of the eye diagram analysis for the error number.

## Parameters

| Name | Type | Description |
|---|---|---|
| handle |  | A unique ID. The same handle must be used as for the eye diagram analysis call with the function testWaitScopePerformEyeDiagramAnalysis |
| Keyword | Description | Type |
| handle | A unique ID | long |
| frame |  | Returns the relevant data for the frame where the error occurred. |
| errorNo |  | The error number the data are requested. |
| data |  | The serial bit analysis violation data for the error number. See ScopeSerialBitAnalysisViolationData. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | 13.0 | — | — | 3.0 SP3 |
| Restricted To | — | CAN LIN FlexRay Scope | CAN LIN FlexRay Scope | — | — | CAN LIN FlexRay Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
