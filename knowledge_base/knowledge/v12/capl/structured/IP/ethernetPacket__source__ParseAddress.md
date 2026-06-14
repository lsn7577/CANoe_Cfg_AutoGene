# ethernetPacket::source::ParseAddress

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.source.ParseAddress( char addressAsString[] ); // form 1
```

## Description

Sets the source or destination MAC address of an Ethernet packet with a string.

The address must be given in this form: 02:00:00:12:34:AB

## Example

```c
ethernetPacket pkt;

pkt.source.ParseAddress( "02:00:00:00:00:01" );
pkt.destination.ParseAddress( "FF:FF:FF:FF:FF:FF" );
```

## Availability

| Since Version |
|---|
