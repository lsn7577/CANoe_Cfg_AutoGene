# ethernetPacket

> Category: `IP` | Type: `function`

## Syntax

```c
ethernetPacket <packet var>;
```

## Description

Can be used to create an Ethernet send object. The object data can be manipulated by selectors associated with this object.

## Example

With Vector network interfaces in operation modes which supports more than 1 hardware channel, the selector hwChannel can be set to output on a specific hardware channel. If the hwChannel is not set or 0, the transfer function decides on which hardware channel(s) the packet is sent.

```c
ethernetPacket txPacket;
int i;

txPacket.msgChannel  = 1;
txPacket.hwChannel   = 2;
txPacket.source      = EthGetMacAddressAsNumber( "20:00:00:00:00:01" );
txPacket.destination = EthGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
txPacket.Length      = 100;
txPacket.type        = 0xF123;

for( i = 0; i < txPacket.Length; i++ )
{
  txPacket.Byte(i) = i & 0xFF;
}
output( txPacket );
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| time_ns Point in time, units: nanoseconds | int64 | Read only |
| dir Direction of transmission, event classification; possible values: Rx, Tx | byte | Read only |
| msgChannel Application channel, i.e. Eth 1 | word |  |
| hwChannel Hardware channel. If not supported by network interface, value is 1. | word | Only with Vector Interfaces, i.e. VN5640, with operation mode with more than 1 hardware channel. |
| Length Length of Ethernet payload data (starting after the Ethertype). | word |  |
| FCS Ethernet frame checksum. For some Ethernet hardware this value is not available (value 0). | dword | Read only |
| FrameLen Frame duration in ns. For some Ethernet hardware this value is not available (value 0). | int64 | Read only |
| SOF Start-of-Frame time stamp in ns. For some Ethernet hardware this value is not available (value 0). | int64 | Read only |
| Type Ethertype | word |  |
| Source Source Ethernet MAC address. Only 6 bytes of the QWord are used and network byte order is used. | qword |  |
| Destination Destination Ethernet MAC address. Only 6 bytes of the QWord are used and network byte order is used. | qword |  |
| byte(x) Message data byte (unsigned 8 bit); Offset 0 is the byte directly after the Ethertype. | byte |  |
| char(x) Message data byte (signed 8 bit); Offset 0 is the byte directly after the Ethertype. | char |  |
| word(x) Message data word (unsigned 16 bit); Offset 0 is the word directly after the Ethertype. | word |  |
| int(x) Message data word (signed 16 bit); Offset 0 is the int directly after the Ethertype. | int |  |
| dword(x) Message data word (unsigned 32 bit); Offset 0 is the dword directly after the Ethertype. | dword |  |
| long(x) Message data word (signed 32 bit); Offset 0 is the long directly after the Ethertype. | long |  |
| qword(x) Message data word (unsigned 64 bit); Offset 0 is the qword directly after the Ethertype. | qword |  |
| int64(x) Message data word (signed 64 bit); Offset 0 is the int64 directly after the Ethertype. | int64 |  |
| Simulated Message has been sent by a simulated CAPL node; possible values: 0 (no), 1 (yes) | byte | Read only |
| <protocol>.byte/word/dword/qword/char/int/int64/long | byte, word, dword, qword, char, int, int64, long |  |
| <protocol>.byteLength | long | Read only |
| <protocol>.byteOffset | long | Read only |
| <protocol>.<field> | byte, word, dword, qword (depends on field) |  |
| <protocol>.<field>.bitLength | long | Read only |
| <protocol>.<field>.bitOffset | long | Read only |
| <protocol>.<field>.byteLength | long | Read only |
| <protocol>.<field>.byteOffset | long | Read only |
| <protocol>.<optional-structure>.<field> | byte, word, dword, qword (depends on field) |  |
| <protocol>.byte/word/dword/qword/char/int/int64/long | ../Selectors/CAPLfunctionProtocolByte.htm |  |
| <protocol>.byteLength | ../Selectors/CAPLfunctionProtocolByteLength.htm |  |
| <protocol>.byteOffset | ../Selectors/CAPLfunctionProtocolByteOffset.htm |  |
| <protocol>.<field> | ../Selectors/CAPLfunctionProtocolField.htm |  |
| <protocol>.<field>.bitLength | ../Selectors/CAPLfunctionProtocolFieldBitLength.htm |  |
| <protocol>.<field>.bitOffset | ../Selectors/CAPLfunctionProtocolFieldBitOffset.htm |  |
| <protocol>.<field>.byteLength | ../Selectors/CAPLfunctionProtocolFieldByteLength.htm |  |
| <protocol>.<field>.byteOffset | ../Selectors/CAPLfunctionProtocolFieldByteOffset.htm |  |
| <protocol>.<optional-structure>.<field> | ../Selectors/CAPLfunctionProtocolOptionalStructureField.htm |  |
