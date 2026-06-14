# C2xAddToken

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xAddToken( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function adds an additional token at the end of a protocol header

## Return Values

0 or error code

## Example

```c
long packetHandle = 0;
packetHandle = C2xInitPacket("wsmp");
C2xAddToken(packetHandle, "wsmp", "transmitPower");
C2xAddToken(packetHandle, "wsmp", "dataRate");
C2xAddToken(packetHandle, "wsmp", "channelNumber");
C2xCompletePacket(packetHandle);
C2xOutputPacket(packetHandle);
```

## Availability

| Since Version |
|---|
