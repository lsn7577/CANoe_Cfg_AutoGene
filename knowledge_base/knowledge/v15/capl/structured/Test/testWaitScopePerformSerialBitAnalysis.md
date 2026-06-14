# testWaitScopePerformSerialBitAnalysis

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopePerformSerialBitAnalysis (linframe aMessage, dword flags, dword msgFieldStart, dword msgFieldEnd, ScopeBitMaskPolygon bitMaskPolygon, long domVoltageThreshold , long recVoltageThreshold, ScopeAnalyseHandle handle);
```

## Description

Checks the bits of a LIN message against the defined bit mask.

## Parameters

| Name | Type | Description |
|---|---|---|
| aMessage |  | The LIN message to be analyzed. |
| flags |  | Reserved must be set to 0. |
| msgFieldStart, msgFieldEnd |  | The start and end of the cutout to be fitted. See ScopeBitAnalyse.cin. |
| Keyword | Description | Type |
| maskPointCount | Count of the points in the mask-arrays | long |
| data_0_Mask | Voltage level in mV for dominant bits | long[] |
| data_1_Mask | Voltage level in mV for recessive bits | long[] |
| timeOffset | Relative position within bit in percent | double[] |
| domVoltageThreshold, recVoltageThreshold |  | The voltage levels in millivolt used from the bit parser for detecting dominant and recessive bits. |
| Keyword | Description | Type |
| handle | A unique ID | long |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | LIN Scope | LIN Scope | — | — | LIN Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
