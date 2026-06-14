# OnMostEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostEthPkt(long pktDataLen);
```

## Description

When an Ethernet packet is received over the Packet Data Channel the OnMostEthPkt event procedure is called.

The following functions are available for evaluating the event:

Returns the channel of the packet event.

Returns the time stamp of the event (Units: 10 µs).

Returns the time stamp of the event (Units: 1 ns).

Returns the hardware generated time stamp of the event (Units: 10 µs).

Returns the 48 bit source or destination Ethernet address.

Returns the direction of transmission (Rx=0, Tx=1, TxRe-quest=2).

Number of transported data bytes.

Tries to copy cnt data bytes to a provided buffer. Returns the actual number of copied bytes.

Tries to copy cnt data bytes starting at byte position 'begin' to a provided buffer. Returns the actual number of copied bytes.

Returns 1 if the packet was received over the Spy of the Packet Data Channel, otherwise 0.

Returns the acknowledge code.

Returns the preemptive acknowledge code (for mostEthPktIsSpy()=1 only).(0x00: No Response; 0x01: Buffer full; 0x04: OK)

Returns the CRC value (for mostEthPktIsSpy()=1 only).

Returns the CRC acknowledge code (for mostEthPktIsSpy()=1 only).(0x00: No Response; 0x01: CRC error; 0x04: OK)

In nodal sequences (Measurement Setup) a received packet can be passed to the next node by the outputMostEthPktThis command.

## Parameters

| Name | Description |
|---|---|
| pktDataLen | Number of data bytes of the packet. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP2 | 7.1 SP2 | 13.0 | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | MOST150 | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | —✔ |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | ✔ | — | — | —✔ |
