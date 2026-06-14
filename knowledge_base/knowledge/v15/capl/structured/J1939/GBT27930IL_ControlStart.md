# GBT27930IL_ControlStart

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_ControlStart(); // form 1
long GBT27930IL_ControlStart(dbNode node); // form 2
long GBT27930IL_ControlStart( byte address ); // form 3
long GBT27930IL_ControlStart(dbNode node, byte address ); // form 4
```

## Description

The node starts the cyclic transmission of the configured messages.

The source address can be specified optionally. If it is not specified the node attribute NmStationAddress must be defined.

## Parameters

| Name | Description |
|---|---|
| address | source address of the node (optional) |
| node | Simulation node to apply the function |

## Return Values

0 on success or IL Error Code

## Example

```c
on start
{
GBT27930IL_ControlStart();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12: form 1, 3 12.0: form 2, 4 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | (form 2, 4) J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
