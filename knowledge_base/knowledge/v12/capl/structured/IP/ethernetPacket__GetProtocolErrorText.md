# ethernetPacket::GetProtocolErrorText

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.GetProtocolErrorText( char buffer[] );
```

## Description

Copies an error text to the buffer for invalid Ethernet packets. For valid Ethernet packets an empty string is returned.

## Return Values

Number of characters copied to buffer.

## Example

```c
on ethernetPacket *
{
  if (this.HasProtocolError())
  {
    char text[100]
    pkt.GetProtocolError( text );
    write( "Protocol error on Eth %d: %s", this.msgChannel, text );
  }
}
```

## Availability

| Since Version |
|---|
