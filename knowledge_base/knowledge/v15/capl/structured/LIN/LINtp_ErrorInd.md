# LINtp_ErrorInd

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_ErrorInd(int error);
```

## Description

This callback is called when an error on the transport layer occurs.

## Parameters

| Name | Description |
|---|---|
| Error | 1: Timeout during wait for CF 2: Timeout during wait for FC 3: Received wrong SN 4: TxBusy, only one transmission has taken place to a moment 5: Unexpected PDU received 6: Timeout while trying to send a CAN message 7: Too many FC.WFT sent 8: Receive buffer overflow 9: Wrong parameter <0: Unknown error The abbreviations are described in OSEK TP. |

## Return Values

Error

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | — | — | — | — | — |
| Restricted To | — | LIN Real bus mode | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
