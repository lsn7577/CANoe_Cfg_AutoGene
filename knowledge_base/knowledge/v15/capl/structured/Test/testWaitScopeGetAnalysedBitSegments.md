# testWaitScopeGetAnalysedBitSegments

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetAnalysedBitSegments(long bitNumber, ScopeAnalyseBitSegmentData segmentData, dword noOfSegments);
```

## Description

Request the analysis data for a single bit. The analysis data are calculated by calling the function testWaitForScopeAnalyseBitSegments.

## Parameters

| Name | Type | Description |
|---|---|---|
| bitNumber |  | The bit number the data are requested.The number must be between 0 and the return value of the function testWaitForScopeAnalyseBitSegments. |
| Keyword | Description | Type |
| SegmentStart | Start of segment within bit in % | dword |
| SegmentEnd | End of segment within bit in % | dword |
| BitField | Scope enum for bit type or field type. See ScopeBitAnalyse.cin | dword |
| BitNo | Number of bit within bit field | dword |
| BitLevel | 0 – dominant bit level 1 – recessive bit level | dword |
| ReferenceVoltage | Voltage of reference point in mV | dword |
| MinVoltage | Minimal voltage within the segment in mV | dword |
| MaxVoltage | Maximal voltage within the segment in mV | dword |
| AvgVoltage | Average voltage within the segment in mV | dword |
| noOfSegments |  | Number of the bit segments. The Number should be the same used by the function testWaitForScopeAnalyseBitSegments (maximum = 10). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | 13.0 | — | — | 2.2 SP2 |
| Restricted To | — | CAN Scope | CAN Scope | — | — | CAN Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
