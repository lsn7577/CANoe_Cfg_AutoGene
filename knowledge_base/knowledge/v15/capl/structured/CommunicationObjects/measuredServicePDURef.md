# measuredServicePDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredServicePDURef * <var>; // form 1
measuredServicePDURef <PDU> <var>; // form 2
measuredServicePDURef <Datatype> <var>; // form 3
```

## Description

References a service PDU measurement point, which means measuring a specific connection between consumer and provider for a service PDU.

Not used for PDUs outside services, the data type of these is measuredPDURef.

## Parameters

| Name | Description |
|---|---|
| PDU | PDU, determining the data type of the object. |
| Datatype | Data type of the object (a PDU definition). |

## Example

```c
measuredServicePDURef MirrorAdjustment.StatusPDU pdu1;
pdu1 = MirrorAdjustment.measure[CANoe,LeftMirror].StatusPDU;
write("Latest x: %d", $pdu1.Position.x);
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
