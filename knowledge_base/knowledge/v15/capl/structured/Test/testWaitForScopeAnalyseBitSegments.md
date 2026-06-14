# testWaitForScopeAnalyseBitSegments

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeAnalyseBitSegments(message aMessage, ScopeAnalyseBitSegment bitSegments[], dword noOfSegments, dword referenceVoltagePoint, dword flags, dword msgFieldStart, dword msgFieldEnd);
```

## Description

Starts an analysis for the defined bit segments for each bit, which is within the defined range. The result of the analysis can be requested with the function testWaitScopeGetAnalysedBitSegments.

## Parameters

| Name | Type | Description |
|---|---|---|
| aMessage |  | The message where the bits should be analyzed. |
| Keyword | Description | Type |
| SegmentStart | Start of the bit segment in percent of the bit length (100% = nominal bit length) | dword |
| SegmentEnd | End of the bit segment in percent of the bit length (100% = nominal bit length) | dword |
| noOfSegments |  | Number of the bit segments used for the analysis. |
| referenceVoltagePoint |  | The reference voltage point within the bit in %. |
| Bits |  | Description |
| 0 |  | CAN high signal used for analysis |
| 1 |  | CAN low signal used for analysis |
| 2 |  | CAN diff signal used for analysis |
| 3 |  | CAN common mode voltage (CMV) used for analysis |
| msgFieldStart, msgFieldEnd |  | Start and end field of the bit range. See ScopeBitAnalyse.cin |

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
