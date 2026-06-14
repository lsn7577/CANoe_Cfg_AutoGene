# on PDU

> Category: `Other` | Type: `event`

## Description

This event procedure is called if the corresponding PDU is received of which the updated bit is set or undefined. For the event procedure of type * and [*] keyword this is an untyped PDU object. For all other event procedures keyword this is a typed PDU object.

## Example

Example 1

Example 2

Example 3

```c
on PDU short 5
{
  write("on pdu: %s", this.name);
}
on PDU EngineData
{
  write("EngineData received at: %d s", this.time);
}
on PDU *
{
  write( "on pdu: LongHeaderID %X length %d", this.LongHeaderID, this.PduLength );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 9.0 SP3) SOME/IP PDU only with on PDU * (since version 10.0 SP4) | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 9.0 SP3) SOME/IP PDU only with on PDU * (since version 10.0 SP4) | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 9.0 SP3) SOME/IP PDU only with on PDU * (since version 10.0 SP4) | — | — | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs (since version 2.1 SP3) SOME/IP PDU only with on PDU * (since version 2.2 SP4) |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
