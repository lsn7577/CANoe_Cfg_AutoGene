# KLine_SetFunctionalAddress

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetFunctionalAddress(Byte functionalAddress)
```

## Description

Sets the functional address of the ECU, i.e. it can receive broadcast messages directed at this address.

## Parameters

| Name | Description |
|---|---|
| functionalAddress | Broadcast address used by the tester to address a group of ECUs. |

## Return Values

On success 0, otherwise a value less than 0.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 SP3 | 8.2 SP3 | — | — | — | 1.1 SP2 |
| Restricted To | K-Line Real bus mode ECU tester | K-Line Real bus mode ECU simulation ECU tester | — | — | — | K-Line Real bus mode ECU simulation |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
