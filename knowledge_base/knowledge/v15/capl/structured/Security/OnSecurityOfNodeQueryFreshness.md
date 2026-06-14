# OnSecurityOfNodeQueryFreshness

> Category: `Security` | Type: `function`

## Syntax

```c
long OnSecurityOfNodeQueryFreshness(char nodeName[], char nameName[], dword context, char pduName[], dword dataId, dword freshnessValueId, dword attemptNr, byte payload[], dword payloadLength, qword& freshness, dword& freshnessLength, qword truncatedRxFreshness, dword truncatedRxFreshnessBitLength)
```

## Description

This callback is called for every secured PDU of the specified node on the specified network for which a CMAC has to be calculated of verified.

The callback is triggered before the CMAC calculation starts.

The callback provides the possibility the calculate a freshness value in CAPL and force the Security Manager to use this freshness value for the next CMAC calculation / verification.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | The name of the node. |
| char networkName[] | The name of the network the node is on. |
| dword context | 1: PDU is received (CMAC verification) 0: PDU is transmitted (CMAC calculation) |
| char pduName[] | The name of the PDU. |
| dword dataId | The data ID of the PDU. |
| dword freshnessValueId | The freshness value ID of the PDU. |
| dword attemptNr | The number of the attempted verification. |
| byte payload[] | The payload of the PDU. |
| dword payloadLength | The payload length of the PDU in bytes. |
| qword& freshness [Out] | The freshness the CAPL code provides. |
| dword& freshnessLength [Out] | The freshness length of the freshness the CAPL code provides in bits. |
| qword truncatedRxFreshness | The received freshness (only in case context is 1). |
| dword truncatedRxFreshnessBitLength | The received freshness length in bits (only in case context is 1). |

## Return Values

qword& freshness [Out]The freshness the CAPL code provides.
dword& freshnessLength [Out]The freshness length of the freshness the CAPL code provides in bits.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | Version |
| Restricted To | — | CAN CAN FD FR ETH | — | — | — | e.g. CAN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
