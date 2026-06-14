# testWaitScopeGetSerialBitAnalyseViolationData

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetSerialBitAnalyseViolationData(ScopeAnalyseHandle handle, long errorNo, ScopeDutyCycleDefinition dutyCycle, ScopeBitDataDutyCycle cycleData, ScopeSerialBitAnalysisViolationData data);
```

## Description

Returns the duty cycle data and the violation data of the serial bit analysis for the error number.

## Parameters

| Name | Type | Description |
|---|---|---|
| Keyword | Description | Type |
| handle | A unique ID | long |
| errorNo |  | The error number the data are requested. |
| dutyCycle |  | The duty cycle measurement parameters. See ScopeDutyCycleDefintion. |
| cycleData |  | The duty cycle data for the defined bit. See ScopeBitDataDutyCycle. |
| data |  | The serial bit analysis violation data for the error number. See ScopeSerialBitAnalysisViolationData. |

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
