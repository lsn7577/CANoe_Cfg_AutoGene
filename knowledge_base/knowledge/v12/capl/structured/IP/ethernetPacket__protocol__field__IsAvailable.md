# ethernetPacket::protocol::field::IsAvailable

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.<protocol>.<field>.IsAvailable();
```

## Description

Returns if a protocol field is available in the Ethernet packet. This can be used, if the protocol contains optional fields or options.

## Return Values

1: Protocol field is available

## Example

```c
on ethernetPacket *
{
  if (this.udp.checksum.IsAvailable())
  {
    Write( "Protocol field udp.checksum ist available and has value 0x%X", this.udp.checksum );
  }
}
```

## Availability

| Since Version |
|---|
