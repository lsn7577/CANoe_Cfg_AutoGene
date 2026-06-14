# SecurityOfNodeTransmitApplicationProtocol

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeTransmitApplicationProtocol(char nodeName[], char networkName[], char applicationProtocolUserDefinedId[], byte payload[], dword payloadLength)
```

## Description

Transmits a special message of sequence of message protocol from the specified node on the specified network, specifically to the active Security Profile on the network.

The application protocol is specific to the active Security Profile on the network. Please refer to the Security Source specific manual to get more information about if there are application protocols available and their functionality and purpose.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | The name of the node. |
| char networkName[] | The name of the network the node is on. |
| char applicationProtocolUserDefinedId[] | The Id of the application protocol, which can be specified in the Security Manager GUI. |
| byte payload[] | The payload of the application protocol. |
| dword payloadLength | The length of the payload in bytes. |

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
