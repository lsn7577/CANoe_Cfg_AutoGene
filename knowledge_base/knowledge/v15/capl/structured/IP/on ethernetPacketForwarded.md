# on ethernetPacketForwarded

> Category: `IP` | Type: `event`

## Description

The event procedure is called when the Ethernet network interface has send a received Ethernet packet on one or more other hardware channels, i.e. with VN5640 which is configured as Ethernet switch. It can only be used with network interfaces which supported forwarding of Ethernet packets.

To access the control information you would use selectors.

The key word this is available within an on ethernetPacketForwarded procedure, to access the data of the packet that has just been received.

CAPL programs are by default not transparent to bus events. This means that a CAPL node in the evaluation branch of the measurement configuration will block the data flow to its right side. You must explicitly program the passing of messages in CAPL nodes in the evaluation branch.

To make the CAPL node transparent to messages you would write:

## Example

Example 1

Example 2

```c
on ethernetPacketForwarded *
{
  write("Received Ethernet packet forwarded on Eth%d", this.msgChannel );
  output( this ); // only required in CAPL node in measurement setup!
}
on ethernetPacketForwarded msgChannel1.*
{
  write("Ethernet packet forwarded with length %d", this.length );
  output( this ); // only required in CAPL node in measurement setup!
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP3 | 9.0 SP3 | 13.0 | — | — | 2.1 SP3 |
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

| Selector | Type | Access Limitation |
|---|---|---|
| time_ns Point in time, units: nanoseconds | int64 | Read only |
| dir Direction of transmission, event classification; possible values: Rx, Tx | byte | Read only |
| msgChannel Application channel, i.e. Eth 1 | word | Read only |
| hwChannel Hardware channel. If not supported by network interface, value is 1. | word | Read only |
| Length Length of Ethernet payload data (starting after the Ethertype). | word | Read only |
| FCS Ethernet frame checksum. For some Ethernet hardware this value is not available (value 0). | dword | Read only |
| FrameLen Frame duration in ns. For some Ethernet hardware this value is not available (value 0). | int64 | Read only |
| SOF Start-of-Frame time stamp in ns. For some Ethernet hardware this value is not available (value 0). | int64 | Read only |
| Type Ethertype | word | Read only |
| Source Source Ethernet MAC address. Only 6 bytes of the QWord are used and network byte order is used. | qword | Read only |
| Destination Destination Ethernet MAC address. Only 6 bytes of the QWord are used and network byte order is used. | qword | Read only |
| byte(x) Message data byte (unsigned 8 bit); Offset 0 is the byte directly after the Ethertype. | byte | Read only |
| char(x) Message data byte (signed 8 bit); Offset 0 is the byte directly after the Ethertype. | char | Read only |
| word(x) Message data word (unsigned 16 bit); Offset 0 is the word directly after the Ethertype. | word | Read only |
| int(x) Message data word (signed 16 bit); Offset 0 is the int directly after the Ethertype. | int | Read only |
| dword(x) Message data word (unsigned 32 bit); Offset 0 is the dword directly after the Ethertype. | dword | Read only |
| long(x) Message data word (signed 32 bit); Offset 0 is the long directly after the Ethertype. | long | Read only |
| qword(x) Message data word (unsigned 64 bit); Offset 0 is the qword directly after the Ethertype. | qword | Read only |
| int64(x) Message data word (signed 64 bit); Offset 0 is the int64 directly after the Ethertype. | int64 | Read only |
