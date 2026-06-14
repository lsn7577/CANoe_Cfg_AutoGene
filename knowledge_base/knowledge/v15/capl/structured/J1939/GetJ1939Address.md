# GetJ1939Address

> Category: `J1939` | Type: `function`

## Syntax

```c
long GetJ1939Address (Node aNode);
```

## Description

Gets the current address of a J1939 node even the address has been changed by the J1939 network management.

## Parameters

| Name | Description |
|---|---|
| aNode | The function returns the address of this node. |

## Return Values

Current address of the node

## Example

```c
dword address;
address = GetJ1939Address (N1);
Write("Address of node N1 is = %d", address );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 SP3 | 8.2 SP3 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | J1939 Test nodes | J1939 Test nodes | J1939 Test nodes | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ (since 8.5 SP2) | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
