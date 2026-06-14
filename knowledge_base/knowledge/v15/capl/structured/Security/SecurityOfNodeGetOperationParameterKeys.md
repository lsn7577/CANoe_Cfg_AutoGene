# SecurityOfNodeGetOperationParameterKeys

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeGetOperationParameterKeys(char nodeName[], char networkName[], long category, dword keyBuffer[], dword keyBufferLength)
```

## Description

Gets the list of operation parameter keys, supported by the currently loaded Security Source.

Which and how many operation parameters exist, which values are valid for an operation parameter differs from Security Source to Security Source.

Please refer to the Security Source specific manual to get more information about operation parameters. The manual can be opened from the Vector Security Manager on the OEM specific ribbon page.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | Name of the node. |
| char networkName[] | Name of the network in which the node is located. |
| long category | The category of the operation parameters, 0 = all operation parameters. |
| dword keyBuffer[] | The allocated buffer in which the operation parameter keys are written by the Security Source. [out] |
| dword keyBufferLength | The capacity of the keyBuffer [in], the number of operation parameter keys in the keyBuffer. [out] |

## Return Values

A value of 1 means that the action was successful. A value less than or equal to 0 means error.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP4 | 11.0 SP4 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
