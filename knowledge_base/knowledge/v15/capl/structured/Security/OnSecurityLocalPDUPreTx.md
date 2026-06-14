# OnSecurityLocalPDUPreTx

> Category: `Security` | Type: `function`

## Syntax

```c
void OnSecurityLocalPDUPreTx(char pduName[], dword dataId, byte payload[], dword payloadLength, qword& authInfoHigh, qword& authInfo, dword authInfoBitLength, qword& freshness, dword freshnessBitLength, dword freshnessValueId)
```

## Description

This callback handler is called, after all data updates and the automatic Authenticator (CMAC) calculation has be done. Payload, AuthInfo and freshness can be modified in this handler before the transmission starts. Fault injection and evaluation of new algorithm are typical examples.

## Parameters

| Name | Description |
|---|---|
| char pduName[] | The name of the PDU. |
| dword dataId | The data ID of the PDU. |
| byte payload[] | The payload of the PDU. |
| dword payloadLength | The payload length of the PDU in bytes. |
| qword& authInfoHigh [Out] | Upper 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits.Otherwise 0; |
| qword& authInfo [Out] | The full authenticator value or the lower 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits. |
| dword authInfoBitLength | Length of complete authenticator to transmit( length of authInfo if the authenticator is <= 64 bit, otherwise length of authInfo + authInfoHigh) |
| qword& freshness [Out] | The transmitted freshness value. |
| dword freshnessBitLength | The transmitted freshness value length in bits. |
| dword freshnessValueId | The freshness value ID of the PDU. |

## Example

```c
// this example modifies the MAC of PDU with Data ID 1
void OnSecurityLocalPDUPreTx(char pduName[], dword dataId, byte payload[], dword payloadLength, qword& authInfoHigh, qword& authInfo, dword authInfoBitLength, qword& freshness, dword freshnessBitLength, dword freshnessValueId)
{
  if (dataId == 1)
  {
    authInfo = 0x123456; // change cmac
    // freshness = 0x02; // change freshness
    // payload[0] = 0xFF; // change payload;
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
