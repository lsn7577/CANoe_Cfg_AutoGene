# <OnEthPacket>

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void <OnEthPacket>( long channel, long dir, long packet);
```

## Description

The function is called when a registered Ethernet packet is received.

Within this callback function the following functions can be used to retrieve the received packet data:

The functions access the payload of the highest interpretable protocol. Offset 0 starts at the beginning of the payload.

## Return Values

—

## Example

```c
see example of EthReceivePacket
```

## Availability

| Up to Version |
|---|
