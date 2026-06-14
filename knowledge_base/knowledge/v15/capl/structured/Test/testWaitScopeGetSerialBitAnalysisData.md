# testWaitScopeGetSerialBitAnalysisData

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetSerialBitAnalysisData (ScopeAnalyseHandle handle, dword msgField, dword bitNo, ScopeDutyCycleDefinition dutyCycle, ScopeBitDataDutyCycle data);
```

## Description

Returns the serial bit analysis data and duty cycle data for the defined bit.

## Parameters

| Name | Type | Description |
|---|---|---|
| Keyword | Description | Type |
| handle | A unique ID | long |
| msgField |  | The field within the message. See ScopeBitAnalyse.cin. |
| bitNo |  | The bit number within the msg field. |
| dutyCycle |  | The duty cycle measurement parameters. See ScopeDutyCycleDefintion. |
| data |  | The duty cycle data for the defined bit. See ScopeBitDataDutyCycle. |

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
