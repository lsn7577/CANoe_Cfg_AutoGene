# ethernetPacket::GetData

> Category: `IP` | Type: `method`

## Syntax

```c
word ethernetPacket.GetData(word offset, char dest[], word length); // form 1
word ethernetPacket.GetData(word offset, byte dest[], word length); // form 2
word ethernetPacket.GetData(word offset, struct * dest); // form 3
word ethernetPacket.GetData(word offset, sysvarStruct dest); // form 4
word ethernetPacket.GetData(char protocol[], char field[], byte dest[]); // form 5
```

## Description

Copies the data of an Ethernet packet to a byte array, char array, CAPL struct or system variable struct.

## Parameters

| Name | Description |
|---|---|
| offset | Byte offset of the data in the Ethernet packet. Offset 0 is the byte directly after the Ethertype. |
| dest | Destination where the data is copied to. |
| length | Number of bytes to copy. |

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

  if(this.IsAvailable("tcp", "data"))
  {
    byte buffer[1500];
    word payloadLength;
    payloadLength = this.GetData("tcp", "data", buffer);
   write("tcp payload length: %d", payloadLength);
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0: form 1-4 13.0 SP2: form 5 | 10.0: form 1-4 13.0 SP2: form 5 | 13.0 | — | — | 2.2: form 1-4 5.0 SP2: form 5 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
