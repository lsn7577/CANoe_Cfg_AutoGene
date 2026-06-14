# OnLocalSecurityPDUValidated

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by OnSecurityLocalPDUValidated.

This callback handler is called, when a secured PDU is received in the node. Besides to the verification result all values which have been used for verification can be analyzed.

| Deprecated Function Replaced by OnSecurityLocalPDUValidated. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void OnLocalSecurityPDUValidated(char pduName[], dword dataId, byte payload[], long payloadLength, qword authInfo, dword authInfoBitLength, qword freshness, dword freshnessBitLength, dword verificationResult) |  |  |  |
| Function | This callback handler is called, when a secured PDU is received in the node. Besides to the verification result all values which have been used for verification can be analyzed. |  |  |  |
| Parameters | duName PDU name. |  |  |  |
| dataId Used DataID. |  |  |  |  |
| payload Byte array with the received data. |  |  |  |  |
| payloadLength Length of the payload array in byte. |  |  |  |  |
| authInfo Received authentication (CMAC). |  |  |  |  |
| authInfoBitLength Length of the authentication in bit. |  |  |  |  |
| freshness Received freshness value. |  |  |  |  |
| freshnessBitLength Length of the freshness in bit. |  |  |  |  |
| verificationResult Verification result. 1= verified 0= not verified |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP2 | CAN CAN FD FlexRay Ethernet | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
