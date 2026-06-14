# Class: scopeFieldLengthData

> Category: `Scope` | Type: `notes`

## Description

This structure contains the common bit information for

—

testWaitScopeGetFieldLengthData

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| BitField | The bit field where the bit is contained. | long | Read-only |
| BitNo | The bit number within the field (starts with 0). | dword | Read-only |
| Lenghth | The bit time in ns. | long | Read-only |
| StartTime | The time the bit started in ns. | int64 | Read-only |
| SamplePointVoltage | The voltage of the bit at the sample point. | long | Read-only |
| BitLevel | 0: Dominant 1: Recessive | dword | Read-only |

| Version 15© Vector Informatik GmbH |
|---|
