# testWaitScopeGetMaskViolation

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetMaskViolation (ScopeAnalyseHandle handle, long errorIndex, ScopeMaskViolationData maskViolationData); // form 1
long testWaitScopeGetMaskViolation (ScopeAnalyseHandle handle, long errorIndex, frFrame frame, ScopeMaskViolationData2 maskViolationData); // form 2
```

## Description

Retrieve the data of the bit mask violations found with testWaitScopeAnalyseSignal.

## Parameters

| Name | Type | Description |
|---|---|---|
| Keyword | Description | Type |
| handle | A unique ID | long |
| errorIndex |  | The number of the bit mask error for which the error description shall be returned. |
| Keyword | Description | Type |
| bitField | field type, see ScopeBitAnalyse.cin | long |
| bitNo | bit number within bit field | dword |
| errorType | reserved | dword |
| bitStartTime | bit start in ns | int64 |
| thresholdTimeOffset | distance to bit start in ns | long |
| disturbanceTimeStart | distance of disturbance to bit start in ns | long |
| disturbanceTimeEnd | distance of end of disturbance to bit start in ns | long |
| samplePointVoltage | voltage at sampling point in mV | long |
| domVoltageCANH | voltage at sampling point for dominant bit for signal CAN High | long |
| recVoltageCANH | voltage at sampling point for recessive bit for signal CAN High | long |
| domVoltageCANL | voltage at sampling point for dominant bit for signal CAN Low | long |
| recVoltageCANL | voltage at sampling point for recessive bit for signal CAN Low | long |
| domVoltageDiff | voltage at sampling point for dominant bit for signal CAN Diff | long |
| recVoltageDiff | voltage at sampling point for recessive bit for signal CAN Diff | long |
| V2_V3 | reserved | long |
| thresholdVoltage | threshold level in mV relative to scope ground | long |
| Keyword | Description | Type |
| bitField | field type, see ScopeBitAnalyse.cin | long |
| bitNo | bit number within bit field | long |
| errorType | reserved | dword |
| bitStartTime | bit start in ns | dword |
| disturbanceTimeStart | distance of disturbance to bit start in ps | long |
| disturbanceTimeEnd | distance of end of disturbance to bit start in ps | long |
| Vdist | measured voltage at the point of the maximum disturbance in mV | long |
| Vgiven | expected voltage at the point of the maximum disturbance in mV | long |

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
