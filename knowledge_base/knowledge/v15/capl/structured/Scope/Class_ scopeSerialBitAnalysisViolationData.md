# Class: scopeSerialBitAnalysisViolationData

> Category: `Scope` | Type: `notes`

## Description

This structure contains the violation data for a bit.

—

testWaitScopePerformSerialBitAnalysis | testWaitScopeGetSerialBitAnalyseViolationData

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| BitField | The bit field e.g. LIN Sync Byte Field, of the bit used for the duty cycle measurement. | long | Read-only |
| BitNo | The bit number within the field (starts with 0). | dword | Read-only |
| BitStartTime | The time the bit started in ns. | int64 | Read-only |
| BitLevel | 0: Dominant 1: Recessive | byte | Read-only |
| SamplePointVoltage | The voltage of the bit at the sample point. | long | Read-only |
| DisturbanceTimeStart | Relative time in [ns] to BitStartTime where the violation of the bit mask starts. | long | Read-only |
| DisturbanceStartVoltage | Voltage level in [mV] on the DisturbanceTimeStart. | long | Read-only |
| DisturbanceTimeEnd | Relative time in [ns] to BitStartTime where the violation of the bit mask end. | long | Read-only |
| DisturbanceEndVoltage | Voltage level in [mV] on the DisturbanceTimeEnd. | long | Read-only |
| ScopeSamplePeriod | The sample period of the scope in [ns]. | float | Read-only |
| ScopeVoltageTolerance | The voltage tolerance of the scope measurement probe [mV]. | float | Read-only |

| Version 15© Vector Informatik GmbH |
|---|
