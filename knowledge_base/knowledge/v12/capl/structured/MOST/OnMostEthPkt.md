# OnMostEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostEthPkt(long pktDataLen)
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

## Return Values

—

## Availability

| Since Version |
|---|
