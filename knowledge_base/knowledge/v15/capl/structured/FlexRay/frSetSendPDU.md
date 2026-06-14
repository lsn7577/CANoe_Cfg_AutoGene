# frSetSendPDU

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetSendPDU( <PDU object> );
```

## Description

Configures the hardware to transmit the specified PDU.

All relevant slots are submitted for transmission.

This submission must take place in the On preStart routine in the transmit branch.

If a frPDU object was created using frPDU, it can be submitted for transmission with this function.

## Parameters

| Name | Description |
|---|---|
| <PDU object> | Specifies the PDU object that is to be submitted for transmission. |

## Return Values

—

## Example

For an example see function frUpdatePDU.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.1 | 6.1 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
