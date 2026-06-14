# CAPLfunctionLocalSecurityVerifyAuthenticationInformation

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by SecurityLocalVerifyAuthenticationInformation.

Verifies the specified authentication information (CMAC and freshness) of the PDU. The payload is also an input parameter to the verification logic.

A value <= 0 means error

Value 1 means action was successful.

| Deprecated Function Replaced by SecurityLocalVerifyAuthenticationInformation. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long LocalSecurityVerifyAuthenticationInformation (dword DATAID, byte[] Payload, dword PayloadLength, qword TruncatedAuthenticator, dword TruncatedAuthenticatorBitLength, qword RxFreshnessh, dword RxFreshnessBitLength, qword currentFreshness, dword FreshnessValueBitLength dword ValidationResult) |  |  |  |
| Function | Verifies the specified authentication information (CMAC and freshness) of the PDU. The payload is also an input parameter to the verification logic. |  |  |  |
| Parameters | DATAID Id to lookup the desired key in the security source. |  |  |  |
| Payload Data array |  |  |  |  |
| PayloadLength Length of the payload in byte |  |  |  |  |
| TruncatedAuthenticator Received truncated MAC |  |  |  |  |
| TruncatedAuthenticatorLength Length of the truncated CMAC in bits. |  |  |  |  |
| RxFreshness Received freshness value. |  |  |  |  |
| RxFreshnessBitLength Length of the received (typically truncated) freshness in bits |  |  |  |  |
| currentFreshness Freshness value to be used for calculation |  |  |  |  |
| FreshnessValueBitLength Length of the current freshness in bit |  |  |  |  |
| ValidationResult 1 = valid CMAC 0 = invalid CMAC |  |  |  |  |
| Return Values | A value <= 0 means error Value 1 means action was successful. 1: Success 0: Error, no details -1: Invalid handle -2: data incomplete -3: signal length does not fit -4: Security source error, no details -6: Not supported -10: Security is not usable. Reasons can be: Security Manager version is too old. Tool Version is too old. Security Profile is invalid. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP2 | CAN CAN FD FlexRay Ethernet | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
