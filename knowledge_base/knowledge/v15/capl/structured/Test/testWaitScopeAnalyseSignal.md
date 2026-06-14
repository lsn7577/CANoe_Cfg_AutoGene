# testWaitScopeAnalyseSignal

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeAnalyseSignal (message aMessage, dword flags, dword msgFieldStart, dword msgFieldEnd, ScopeBitMaskPolygon bitMaskPolygon, long domVoltageThreshold , long recVoltageThreshold, ScopeAnalyseHandle handle); // form 1
long testWaitScopeAnalyseSignal (char nodeName[], dword flags, ScopeBitMaskPolygon bitMaskPolygon, ScopeAnalyseResult analyzeResult, ScopeAnalyseHandle handle); // form 2
```

## Description

Form 1: Checks the bits of a CAN message against the defined bit mask.

Form 2: Checks the bits of FlexRay frames which are transmitted by one node against the defined bit mask.

## Parameters

| Name | Type | Description |
|---|---|---|
| aMessage |  | The CAN message to be analyzed. |
| Bits |  | Description |
| 0-2 |  | 0 = Analyze only frames in Key Slots1 = Analyze only frames of static segment2 = Analyze only frames in dynamic segment3 = Use all frame for analysis |
| msgFieldStart, msgFieldEnd |  | The start and end of the cutout to be fitted. See ScopeBitAnalyse.cin |
| Keyword | Description | Type |
| maskPointCount | Count of the points in the mask-arrays | long |
| data_0_Mask | CAN: Voltage level in mV for dominant bits FlexRay: Voltage level in mV for Data0 | long[] |
| data_1_Mask | CAN: Voltage level in mV for recessive bits FlexRay: Voltage level in mV for Data1 | long[] |
| timeOffset | Relative position within bit in percent | double[] |
| domVoltageThreshold, recVoltageThreshold |  | The voltage levels in millivolt used from the bit parser for detecting dominant and recessive bits. |
| Keyword | Description | Type |
| handle | A unique ID | long |
| nodeName |  | The name of the node. |
| Keyword | Description | Type |
| result | The result of the analysis.1 = pass0 = failed | byte |
| analysedFrameCount | Count of the analyzed frames | long |
| framesWithDecodeFailure | Count of frames with decoding errors | long |
| framesWithMaskViolations | Count of frames with bit mask violations | long |
| bitFailureCount | Count of bits with mask violations | long |

## Return Values

Form 1:
Form 2:

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | CAN FlexRay Scope | CAN FlexRay Scope | — | — | CAN FlexRay Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
