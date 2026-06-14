# txPDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
txPDURef * <var>; // form 1
txPDURef <PDU> <var>; // form 2
txPDURef <Datatype> <var>; // form 3
```

## Description

References a tx PDU endpoint (from where the PDU is sent).

## Parameters

| Name | Description |
|---|---|
| PDU | PDU (in the new communication concept, but not in a service). |
| DataType | Data type of the object. |

## Example

```c
txPduRef StatusPdu pdu1;
pdu1 = StatusPdu.senderSide[CANoe];
$pdu1.StatusSignal = newValue;
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
