# ethernetPacket::GetData

> Category: `IP` | Type: `function`

## Syntax

```c
word ethernetPacket.GetData(word offset, char dest[], word length); // form 1
```

## Description

Copies the data of an Ethernet packet to a byte array, char array, CAPL struct or system variable struct.

## Return Values

Number of bytes copied to the destination buffer.

## Example

```c
on ethernetPacket *
{
  dword ipHeaderLength;
  byte  ipProtocol;

  switch(this.type)
  {
    case 0x0800: // IPv4
    ipHeaderLength = (this.Byte(0) & 0x0F) * 4;
    ipProtocol     = this.Byte(9);

    switch(ipProtocol)
    {
      case 17:
      HandleUDP( this, ipHeaderLength+8, swapWord(this.Word(ipHeaderLength)), swapWord(this.Word(ipHeaderLength+2)) );
      break;
    }

    break;
  }
}

void HandleUDP( ethernetPacket * pkt, word udpDataOffset, word srcPort, word dstPort )
{
  char buffer[100];
  word length;

  length = pkt.GetData( udpDataOffset, buffer, elcount(buffer)-1 );
  buffer[length] = 0; // terminating zero for strings

  write( "UDP (port 0x%X to 0x%X): %s", srcPort, dstPort, buffer );
}
```

## Availability

| Since Version |
|---|
