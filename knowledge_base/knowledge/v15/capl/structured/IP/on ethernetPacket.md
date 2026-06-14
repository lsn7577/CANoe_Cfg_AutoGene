# on ethernetPacket

> Category: `IP` | Type: `event`

## Description

The event procedure is called on the receipt of a valid Ethernet packet.

To access the control information you would use selectors.

The key word this is available within an on ethernetPacket procedure, to access the data of the packet that has just been received.

CAPL programs are by default not transparent to bus events. This means that a CAPL node in the evaluation branch of the measurement configuration will block the data flow to its right side. You must explicitly program the passing of messages in CAPL nodes in the evaluation branch.

To make the CAPL node transparent to messages you would write:

## Example

Example 1

Example 2

Example 3

```c
on ethernetPacket *
{
  write("Received Ethernet packet on Eth%d", this.msgChannel );
  output( this ); // only required in CAPL node in measurement setup!
}
on ethernetPacket msgChannel1.*
{
  write("Received Ethernet packet with length %d", this.Length );
  output( this ); // only required in CAPL node in measurement setup!
}
on ethernetPacket ethernetPort::Ethernet1::HU.*
{
  write("Received Ethernet packet with length %d", this.Length );
  output( this ); // only required in CAPL node in measurement setup!
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1, 2 12.0 SP4: form 3 | 8.5: form 1, 2 12.0 SP4: form 3 | 13.0 | — | — | 2.0 SP2: form 1, 2 5.0: form 3 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |

## Selectors

| ethernetErrorPacket | ../Objects/CAPLfunctionEthernetErrorPacket.htm |
|---|---|
