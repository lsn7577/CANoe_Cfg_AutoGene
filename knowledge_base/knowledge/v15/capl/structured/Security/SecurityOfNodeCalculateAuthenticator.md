# SecurityOfNodeCalculateAuthenticator

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeCalculateAuthenticator(char nodeName[], char networkName[], dword dataId, byte payload[], dword payloadLength, qword truncatedAuthenticatorHigh, qword truncatedAuthenticator, dword truncatedAuthenticatorBitLength, qword freshness, dword truncatedFreshnessBitLength, dword freshnessValueBitLength, dword freshnessValueId)
```

## Description

Calculate the authenticator from arbitrary data. The (complete) freshness value must be provided in the function call. Other freshness sources will be ignored. The method returns the truncated freshness via freshness' parameter. The calculated authenticator is returned via the TruncatedAuthenticator parameter. The truncated bit lengths of the authenticator and freshness can be modified.

The result of this method depends on the security profile which is mapped on the network.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | The name of the node. |
| networkName | The name of the network the node is on. |
| char networkName[] | The name of the network the node is on. |
| dword dataId | The data ID of the PDU to lookup the desired key in the security source. |
| byte payload[] | The payload of the PDU. |
| dword payloadLength | The payload length of the PDU in bytes. |
| qword truncatedAuthenticatorHigh [Out] | Upper 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits.Otherwise 0; |
| qword truncatedAuthenticator [Out] | The full authenticator value or the lower 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits. |
| dword truncatedAuthenticatorBitLength [In/Out] | Length of complete authenticator to transmit( length of authInfo if the authenticator is <= 64 bit, otherwise length of authInfo + authInfoHigh) |
| qword freshness [In/Out] | In: The freshness value for CMAC calculation. Out: Truncated freshness. |
| dword truncatedFreshnessBitLength [In/Out] | The length of the truncated freshness in bits. |
| dword freshnessValueBitLength | The freshness value length in bits. |
| dword freshnessValueId | The freshness value ID of the PDU. |

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
