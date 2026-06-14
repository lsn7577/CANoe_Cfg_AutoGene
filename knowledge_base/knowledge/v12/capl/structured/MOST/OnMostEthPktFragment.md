# OnMostEthPktFragment

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostEthPktFragment()
```

## Description

The event procedure OnMostEthPktFragment is called when the spy detects an incomplete Ethernet packet transmission.

The following functions are available for evaluating the event:

Returns the channel of the packet event.

Returns the time stamp of the event (Units: 10 µs).

Returns the time stamp of the event (Units: 1 ns).

Returns the hardware generated time stamp of the event (Units: 10 µs).

Number of transported data bytes.

Tries to copy cnt data bytes to a provided buffer. Returns the actual number of copied bytes.

Due to performance reasons only the first transmitted data bytes are stored in the fragment event.

All following functions return -1 if the corresponding data field is invalid (i.e. event was too short to contain the information).

Returns the 48 bit source or destination Ethernet address.

Returns the acknowledge code.

Returns the preemptive acknowledge from the potential packet receiver(s) to the packet transmitter.

Returns the CRC value.

Returns the CRC acknowledge code.

Returns the announced data length at start of transmission. In general, the announced length is not equal to the actual number of transmitted data bytes for fragments.

In nodal sequences (Measurement Setup) a fragment can be passed to the next node by the outputMostEthPktFragmentThis command.

## Return Values

—

## Availability

| Since Version |
|---|
