# Class: scopeDutyCycleDefinition

> Category: `Scope` | Type: `notes`

## Description

This structure defines the threshold levels for the duty cycle measurement.

—

testWaitScopePerformSerialBitAnalysis | testWaitScopeGetSerialBitAnalysisData | Class: scopeDutyCycleDefinition

| Threshold | Description |
|---|---|
| THRec(max) | Maximum voltage level of a recessive bit |
| THDom(max) | Maximum voltage level of a dominant bit |
| THRec(min) | Minimum voltage level of a recessive bit |
| THDom(min) | Minimum voltage level of a recessive bit |

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| THDomMin | Defines the minimal voltage level for a dominant bit level in mV. | long | Read/Write |
| THDomMax | Defines the maximal voltage level for a dominant bit level in mV. | long | Read/Write |
| THRecMin | Defines the minimal voltage level for a recessive bit level in mV. | long | Read/Write |
| THRecMax | Defines the maximal voltage level for a recessive bit level in mV. | long | Read/Write |

| Version 15© Vector Informatik GmbH |
|---|
