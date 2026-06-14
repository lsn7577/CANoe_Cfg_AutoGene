# OnMostPktFragment

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostPktFragment();
```

## Description

The event procedure OnMostPktFragment is called when the spy detects an incomplete transmission on the Packet Data channel.

The following functions are available for evaluating the event:

Returns the channel of the packet event.

Returns the time stamp of the event (Units: 10 µs).

Returns the time stamp of the event (Units: 1 ns).

Returns the hardware generated time stamp of the event (Units: 10 µs).

Number of transported data bytes.

Tries to copy cnt data bytes to a provided buffer. Returns the actual number of copied bytes.

All following functions return -1 if the corresponding data field is invalid (i.e. event was too short to contain the information).

Returns the source or destination address.

Returns the acknowledge code.

Returns the preemptive acknowledge from the potential packet receiver(s) to the packet transmitter.

Returns the packet index. The packet index increments by one per message from a node.

Returns the CRC value.

Returns the CRC acknowledge code.

Returns the announced data length at start of transmission. In general, the announced length is not equal to the actual number of transmitted data bytes for fragments.

In nodal sequences (Measurement Setup) a fragment can be passed to the next node by the outputMostPktFragmentThis command.

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 SP2: MOST150 7.2 SP3: MOST50 | 7.1 SP2: MOST150 7.2 SP3: MOST50 | — | — | — | —✔ |
| Restricted To | MOST50 MOST150 | MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
