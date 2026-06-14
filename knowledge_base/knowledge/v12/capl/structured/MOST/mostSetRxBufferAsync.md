# mostSetRxBufferAsync

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetRxBufferAsync (long channel, long buffermode)
```

## Description

Starts or stops draining of the asynchronous receive buffer and thereby allows to provoke low level retries.

VN2640: The node may receive a varying number of packets (MDP or MEP) before it eventually provokes low level retries. The number depends on the size of the packets and is limited either to 3 kByte of data or 255 packets.After enabling the draining of the Rx buffer again, a number of packets received during the stress mode may be shown in the Trace with time stamps close to the time of re-enabling the draining.

OptoLyzer G2 3150o: The stress network interface controller (NIC) must have its bypass opened (see mostSetStressNodeParameter).Only packets addressed to the StressNIC will be blocked.

## Return Values

0

## Availability

| Since Version |
|---|
