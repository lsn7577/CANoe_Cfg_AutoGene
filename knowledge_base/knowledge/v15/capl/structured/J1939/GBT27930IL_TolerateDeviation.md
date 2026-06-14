# GBT27930IL_TolerateDeviation

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_TolerateDeviation (long dlcDeviation, long counterpartAddressDeviation); // (form 1)
long GBT27930IL_TolerateDeviation (dbNode node, long dlcDeviation, long counterpartAddressDeviation); // (form 2)
```

## Description

Allows the simulated node to tolerate variations in the address of the other participant and the length of its messages.

## Parameters

| Name | Description |
|---|---|
| dlcDeviation | 0: simulated nodes must not tolerate any deviation in the length of the messages of the other participant 1: simulated node must tolerate deviations in the length of messages of the other participant. |
| counterpartAddressDeviation | 0: simulated nodes must not tolerate any deviation in the address of the other participant 1: simulated node must tolerate deviations in the address of the other participant. |
| node | Simulation node to apply the function |

## Example

Example

```c
—
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 2.0 |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | form 2 J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
