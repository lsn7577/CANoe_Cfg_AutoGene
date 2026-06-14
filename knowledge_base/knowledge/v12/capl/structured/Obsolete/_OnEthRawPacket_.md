# <OnEthRawPacket>

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void <OnEthRawPacket>( long channel, long dir, long packetLength );
```

## Description

The function is called when a registered raw Ethernet packet is received.

Within this callback function the following functions can be used to retrieve the received packet data:

The functions access the raw Ethernet data. Offset 0 starts at the beginning of the Ethernet header.

## Return Values

—

## Example

```c
see example of EthReceiveRawPacket
```

## Availability

| Up to Version |
|---|
