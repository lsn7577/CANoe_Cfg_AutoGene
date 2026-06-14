# ethernetPacket::Clear

> Category: `IP` | Type: `function`

## Syntax

```c
void ethernetPacket.Clear();
```

## Description

Clears data and resets length.

## Return Values

—

## Example

```c
ethernetPacket pkt;

// prepare packet for first output
pkt.ipv6.Init();
pkt.udp.Init();
pkt.udp.SetData( 0, "Hello", 5 );
pkt.CompletePacket();
output( pkt );

// clear the packet
pkt.Clear();

// prepare packet for second output with different
// protocols and data than with first output above

pkt.tcp.Init();
pkt.CompletePacket();
output( pkt );
```

## Availability

| Since Version |
|---|
