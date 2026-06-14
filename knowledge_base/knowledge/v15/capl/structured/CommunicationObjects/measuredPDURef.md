# measuredPDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredPDURef * <var>; // form 1
measuredPDURef <PDU> <var>; // form 2
measuredPDURef <Datatype> <var>; // form 3
```

## Description

References a PDU measurement point, which means measuring a specific connection between sender and receiver for a PDU.

Not used for service PDUs, the data type of these is measuredServicePDURef.

## Parameters

| Name | Description |
|---|---|
| PDU | PDU, determining the data type of the object. |
| Datatype | data type of the object (a PDU definition). |

## Example

```c
measuredPDURef StatusPDU pdu1;
pdu1 = StatusPDU.measure[LeftMirror,CANoe];
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
