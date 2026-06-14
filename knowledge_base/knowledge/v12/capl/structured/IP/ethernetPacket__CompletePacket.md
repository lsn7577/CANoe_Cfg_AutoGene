# ethernetPacket::CompletePacket

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.CompletePacket();
```

## Description

Calculates the checksum and length field for all protocols contained in the packet. The protocols will be valid, after calling this method and the packet can be sent.

## Return Values

0: Success

## Availability

| Since Version |
|---|
