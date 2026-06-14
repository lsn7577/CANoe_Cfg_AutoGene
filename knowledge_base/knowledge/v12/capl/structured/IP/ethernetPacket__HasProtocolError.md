# ethernetPacket::HasProtocolError

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.HasProtocolError();
```

## Description

Returns 1, if the IP protocols of the Ethernet packet contains protocol errors, like wrong checksum or wrong length field, etc.Use ethernetPacket::GetProtocolErrorText to get a description of the error.

## Return Values

0: No protocol error detected

## Example

```c
on ethernetPacket *
{
  if (this.hasProtocolError())
  {
    char text[100]
    pkt.GetProtocolErrorText( text );
    write( "Protocol error on Eth %d: %s", this.msgChannel, text );
  }
}
```

## Availability

| Since Version |
|---|
