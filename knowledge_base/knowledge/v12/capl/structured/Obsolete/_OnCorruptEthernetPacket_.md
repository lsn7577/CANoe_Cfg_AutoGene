# <OnCorruptEthernetPacket>

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void <OnCorruptEthernetPacket>( long channel, long errorCode, long packetLength );
```

## Description

This callback function is called when a corrupt Ethernet packet is received.

Within this callback function the following functions can be used to retrieve the received packet data:

The functions access the raw Ethernet data. Offset 0 starts at the beginning of the Ethernet header.

## Return Values

—

## Availability

| Up to Version |
|---|
