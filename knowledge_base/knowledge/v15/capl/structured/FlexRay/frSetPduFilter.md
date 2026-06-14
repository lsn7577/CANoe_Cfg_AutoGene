# frSetPduFilter

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetPduFilter(frPDU message, long mode);
```

## Description

The function configures a filter for PDUs. With this filter it is possible to receive single PDUs with update bit = 0.

The function overrides the network hardware setting Show PDUs with disabled Update Bit(CANoe menu path: Configuration|Network Hardware...|FlexRay|Options).

The advantage of this filter is that only dedicated PDUs with disabled update bit are received instead of all PDUs with disabled update bit in the network.

## Parameters

| Name | Description |
|---|---|
| message | Name of the PDU to be filtered. |
| Value | Meaning |
| 0 | PDU reception disabled |
| 1 | PDU with update bit = 1 will be received |
| 2 | PDU will be received, the update bit is not evaluated |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP3 | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
