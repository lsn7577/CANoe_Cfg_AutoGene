# testWaitForScopeShowEyeDiagram

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeShowEyeDiagram(message frame, dword groupNumber, ScopeAnalyseHandle handle); // form 1
long testWaitForScopeShowEyeDiagram (linFrame frame, dword groupNumber, ScopeAnalyseHandle handle); // form 2
long testWaitForScopeShowEyeDiagram(frFrame frame, dword groupNumber, ScopeAnalyseHandle handle); // form 3
long testWaitForScopeShowEyeDiagram(char nodeName[],dword groupNumber, ScopeAnalyseHandle handle); // form 4
```

## Description

Show the eye diagram for a single frame or a node without analysis.

## Parameters

| Name | Type | Description |
|---|---|---|
| frame |  | The used CAN, LIN or FlexRay frame for the eye diagram. |
| nodeName |  | The node should be used to display the eye diagram. |
| Value |  | Description |
| 0 |  | Standard Range for a CAN Frame |
| 1 |  | Arbitration Range for a CAN Frame |
| 2 |  | Acknowledge Field CAN Frame |
| 3 |  | Entire CAN Frame |
| 4 |  | Standard Range for a CAN FD Frame |
| 5 |  | Arbitration Range for a CAN FD Frame |
| 6 |  | Acknowledge Field CAN FD Frame |
| Value |  | Description |
| 0 |  | Standard Range for LIN frame (Header and Response) |
| 1 |  | Only Header for LIN frame |
| 2 |  | Only Response for LIN Frame |
| Value |  | Description |
| 0 |  | Entire FlexRay frame |
| 1 |  | FSS Field |
| 2 |  | Header Segment |
| 3 |  | ProtocolFlags |
| 4 |  | Frame ID |
| 5 |  | Payload Length |
| 6 |  | Header CRC |
| 7 |  | Cycle Count |
| 8 |  | Payload Segment |
| 9 |  | Frame CRC |
| handle |  | A unique ID. |
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
