# providedPDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedPDURef * <var>; // form 1
providedPDURef <PDU> <var>; // form 2
providedPDURef <Datatype> <var>; // form 3
```

## Description

References a provided PDU endpoint, which means a specific combination of consumer and provider for a service PDU on provider side.

## Parameters

| Name | Description |
|---|---|
| PDU | PDU of a service, determining the data type of the object. |
| DataType | Data type of the object (a PDU definition). |

## Example

```c
providedPDURef MirrorAdjustment.StatusPDU pdu1;
pdu1 = MirrorAdjustment.providerSide[CANoe,LeftMirror].StatusPDU;
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
