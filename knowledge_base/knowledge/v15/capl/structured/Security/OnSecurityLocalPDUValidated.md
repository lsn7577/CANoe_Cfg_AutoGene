# OnSecurityLocalPDUValidated

> Category: `Security` | Type: `function`

## Syntax

```c
void OnSecurityLocalPDUValidated(char pduName[], dword dataId, byte payload[], dword payloadLength, qword authInfoHigh, qword authInfo, dword authInfoBitLength, qword freshness, dword freshnessBitLength, dword freshnessValueId, dword verificationResult)
```

## Description

This callback handler is called, when a node received a secured PDU and verified the authentication information.

Apart from the verification result, all values which have been used for verification can be analyzed.

## Parameters

| Name | Description |
|---|---|
| char pduName[] | The name of the PDU. |
| dword dataId | The data ID of the PDU. |
| byte payload[] | The payload of the PDU. |
| dword payloadLength | The payload length of the PDU in bytes. |
| qword authInfoHigh | Upper 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits.Otherwise 0; |
| qword authInfo | The full authenticator value or the lower 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits. |
| dword authInfoBitLength | Length of complete received authenticator ( length of authInfo if the authenticator is <= 64 bit, otherwise length of authInfo + authInfoHigh) |
| qword freshness | The freshness value. |
| dword freshnessBitLength | The freshness value length in bits. |
| dword freshnessValueId | The freshness value ID of the PDU. |
| dword verificationResult | 1: Verification successful, PDU is valid 0: Verification failed, PDU is invalid |

## Return Values

—

## Example

```c
// this example does an write output for every secured pdu which is received.
void OnSecurityLocalPDUValidated(char pduName[], dword dataId, byte payload[], dword payloadLength, qword authInfoHigh, qword authInfo, dword authInfoBitLength, qword freshness, dword freshnessBitLength, dword freshnessValueId, dword verificationResult)
{
  if (verificationResult > 0)
    {
      writeLineEx(1,0," Verification SUCCESSFUL");
    }
    else
    {
      writeLineEx(1,3," Verification FAILED");
    }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | 11.0 SP3 | — | — | 3.0 SP3 |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | CAN CAN FD FR ETH |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
