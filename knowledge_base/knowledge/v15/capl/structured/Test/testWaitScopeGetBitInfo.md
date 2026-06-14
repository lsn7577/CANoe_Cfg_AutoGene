# testWaitScopeGetBitInfo

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetBitInfo(ScopeAnalyseHandle handle, dword msgFieldStart,long startBitNo, dword msgFieldEnd, long EndBitNo, ScopeMaskViolationData data);
```

## Description

After a signal was analyzed with the function testWaitScopeAnalyseSignal, the average values of the voltages of CAN_H, CAN_L, and CAN_Diff are calculated for a defined bit range.

## Parameters

| Name | Type | Description |
|---|---|---|
| Keyword | Description | Type |
| handle | A unique ID | long |
| msgFieldStart, startBitNo, msgFieldEnd, EndBitNo |  | The cutout of the frame to be analyzed. msgFieldStart, msgFieldEnd: See ScopeBitAnalyse.cin startBitNo, endBitNo: A bit index in the message field |
| Keyword | Description | Type |
| bitField | field type, see ScopeBitAnalyse.cin | long |
| bitNo | bit number within bit field | dword |
| errorType | reserved | dword |
| bitStartTime | bit start in ns | long |
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
| disturbanceTimeStart | distance of disturbance to bit start in ns | long |
| disturbanceTimeEnd | distance of end of disturbance to bit start in ns | long |
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
