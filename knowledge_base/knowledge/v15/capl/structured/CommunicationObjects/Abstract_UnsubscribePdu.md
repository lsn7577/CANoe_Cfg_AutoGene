# Abstract_UnsubscribePdu

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_UnsubscribePDU(consumedPDURef * pdu);
```

## Description

Unsubscribes for a service PDU if abstract binding is used. Note that this is more low-level; usually its more convenient to call consumedPduRef::AbstractReleasePdu on the PDU.

## Parameters

| Name | Description |
|---|---|
| pdu | PDU which shall be unsubscribed. |

## Example

```c
Abstract_UnsubscribePDU(MirrorAdjustment.consumerSide[0,0].PositionPDU);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
