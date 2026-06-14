# SecurityLocalVerifyAuthenticationInformation

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalVerifyAuthenticationInformation(dword dataId, byte payload[], dword payloadLength, qword truncatedAuthenticatorHigh, qword truncatedAuthenticator, dword truncatedAuthenticatorBitLength, qword rxFreshness, dword rxFreshnessBitLength, qword currentFreshness, dword freshnessValueLength, dword freshnessValueId, dword verificationResult)
```

## Description

Verifies the specified authentication information (MAC and freshness) of the PDU. The (complete) current freshness value must be provided in the function call. Other freshness sources will be ignored. The payload is also an input parameter to the verification logic.

The result of this method depends on the security profile which is mapped on the network.

## Parameters

| Name | Description |
|---|---|
| dword dataId | Id to lookup the desired key in the security source. |
| byte payload[] | The payload of the PDU. |
| dword payloadLength | The payload length of the PDU in bytes. |
| qword truncatedAuthenticatorHigh | Upper 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits. Otherwise 0. |
| qword truncatedAuthenticator | The full authenticator value or the lower 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits. |
| dword truncatedAuthenticatorBitLength | Length of complete authenticator to transmit( length of authInfo if the authenticator is <= 64 bit, otherwise length of authInfo + authInfoHigh). |
| qword rxFreshness | The received freshness value. |
| dword rxFreshnessBitLength | The length of the received (typically truncated) freshness in bits. |
| qword currentFreshness | The freshness value to be used for calculation. |
| dword freshnessValueBitLength | The length of currentFreshness in bits. |
| dword freshnessValueId | The freshness value ID of the PDU. |
| dword verificationResult [Out] | 1: Valid MAC 0: Invalid MAC |

## Return Values

A Value of 1 means that the action was successful. A value less than or equal to 0 means error.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | 11.0 SP3 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
