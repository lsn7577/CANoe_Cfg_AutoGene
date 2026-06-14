# triggerPDU

> Category: `Other` | Type: `function`

## Syntax

```c
void triggerPDU(pdu myPDU);
```

## Description

Triggers a PDU to be sent. If the PDU has an update bit it will be set. After the PDU was sent the update bit will be reset.

## Return Values

—

## Example

```c
on timer cyclic100ms
{
  PDU randomPDU myPDU;
  myPDU.signal1 = 10;
  myPDU.signal2 = 20;
  triggerPDU(myPDU);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 9.0 SP3) | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 9.0 SP3) | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 9.0 SP3) | — | — | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
