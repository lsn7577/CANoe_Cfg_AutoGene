# testWaitScopePerformEyeDiagramAnalysis

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopePerformEyeDiagramAnalysis(message frame, dword flags, dword groupNumber, ScopeSinglePolygonBitMask bitMask, ScopeAnalyseHandle handle); // form 1
long testWaitScopePerformEyeDiagramAnalysis(linFrame frame, dword flags, dword groupNumber, ScopeSinglePolygonBitMask bitMask, ScopeAnalyseHandle handle); // form 2
long testWaitScopePerformEyeDiagramAnalysis(frFrame frame, dword flags, dword groupNumber, ScopeSinglePolygonBitMask bitMask, ScopeAnalyseHandle handle); // form 3
long testWaitScopePerformEyeDiagramAnalysis(char nodeName[], dword flags, dword groupNumber, ScopeSinglePolygonBitMask bitMask, ScopeAnalyseHandle handle); // form 4
```

## Description

Perform a bit analysis for the eye diagram.

## Parameters

| Name | Type | Description |
|---|---|---|
| frame |  | The CAN, LIN or FlexRay frame should be analysed. |
| nodeName |  | The node should be analysed. |
| Bits |  | Description |
| 0-2 |  | 0 = Analyze only frames in Key Slots 1 = Analyze only frames of static segment 2 = Analyze only frames in dynamic segment 3 = Use all frame for analysis |
| 3 |  | 0 = Do not contain BSS 1 = Contain BSS |
| Value |  | Description |
| 0123456 |  | Standard Range for a CAN Frame Arbitration Range for a CAN Frame Acknowledge Field CAN Frame Entire CAN Frame Standard Range for a CAN FD Frame Arbitration Range for a CAN FD Frame Acknowledge Field CAN FD Frame |
| Keyword |  | Description |
| 012 |  | Standard Range for LIN frame (Header and Response)Only Header for LIN frameOnly Response for LIN Frame |
| Keyword |  | Description |
| 0123456789 |  | Entire FlexRay frameFSS FieldHeader SegmentProtocolFlagsFrame IDPayload LengthHeader CRCCycle CountPayload SegmentFrame CRC |
| bitMask |  | The bit mask should be used for the analysis. (See ScopeSinglePolygonBitMask) |
| handle |  | A unique ID. The same handle must be used to request the violation data with the function testWaitScopeGetEyeDiagramAnalysis. |
| Keyword | Description | Type |
| handle | A unique ID | long |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | CAN LIN FlexRay Scope | — | — | — | CAN LIN FlexRay Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
