# C2xIsTokenAvailable

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xIsTokenAvailable( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function checks, if the specified token is part of the packet.

For ASN.1 based protocols, tokens that are not set are not part of the packet between the functions calls of C2xInitPacket and C2xCompletePacket. For other protocols the non-optional tokens are always part of the packet.

## Return Values

1: token is part of the packet

## Example

```c
long packet;

//create geoNetworking unicast
packet = C2xInitPacket("geoNetworking");

//spvNetAddr is optional but headertype (ht) is unicast per default which contains spvNetAddr
if (!C2xIsTokenAvailable(packet, "geoNetworking","spvNetAddr"))
{
  write("error! spvNetAddr is not available in geoNetworking unicast");
}

//transform packet to geoNetworking broadcast
if (C2xSetTokenInt(packet, "geo_cnh", "ht", 4) != 0)
{
  write("error! C2xSetTokenInt failed");
}
if (C2xResizeToken(packet, "geoNetworking", "header", 384) != 0)
{
  write("error! C2xResizeToken failed");
}

//broadcast does not contain spvNetAddr
if (C2xIsTokenAvailable(packet, "geoNetworking", "spvNetAddr"))
{
write("error! spvNetAddr is available in geoNetworking broadcast");
}
```

## Availability

| Since Version |
|---|
