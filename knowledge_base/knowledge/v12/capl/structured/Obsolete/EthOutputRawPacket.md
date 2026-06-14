# EthOutputRawPacket

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthOutputRawPacket( long packetLength, char packetData );
```

## Description

The function sends a raw Ethernet packet. The packet data must contain the destination (byte 0..5) and source (byte 6..11) MAC address and the Ethernet type (byte 12..13 in Motorola format). After that the user data are contained.

## Return Values

0 or error code

## Example

```c
BYTE rawData[18] = { 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x02, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF1, 0x23, 0x01, 0x02, 0x03, 0x04 };
EthOutputRawPacket( elCount(rawData), rawData ); //with calculated fcs

EthOutputRawPacket(elCount(rawData), 4711, rawData); //with user-defined fcs
```

## Availability

| Up to Version |
|---|
