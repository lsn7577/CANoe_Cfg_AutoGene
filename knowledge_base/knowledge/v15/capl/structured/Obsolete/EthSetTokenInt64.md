# EthSetTokenInt64

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket Selectors: <protocol>.<field> |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthSetTokenInt64( long packet, char protocolDesignatorl[], char tokenDesignator[], int64 value ); // form 1 |  |  |  |
| long EthSetTokenInt64( long packet, char protocolDesignatorl[], char tokenDesignator[], long byteOffset, long length, long networkByteOrder, int64 value ); // form 2 |  |  |  |  |
| Function | The function sets the integer value of a token. Form 2 with byte offset sets a part of the token data as integer. |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| protocolDesignator name of the protocol, e.g. "ipv4" |  |  |  |  |
| tokenDesignator name of the token, e.g. "source" |  |  |  |  |
| byteOffset offset from the beginning of the token in byte |  |  |  |  |
| length length of the integer value, up to 8 byte |  |  |  |  |
| networkByteOrder 0: INTEL (little-endian) 1: MOTOROLA (big-endian) |  |  |  |  |
| value new integer value |  |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.6 SP3-12.0 | Ethernet | — | • |  |
| Example long packetHandle;char error[100];int64 srcMacId = 0x5826C8FD2421LL;int64 dstMacId = 0xFFFFFFFFFFFFLL;// create packetpacketHandle = EthInitPacket("eth");if (EthGetLastError() == 0){ // set MAC address EthSetTokenInt64( packetHandle, "eth", "source" , srcMacId ); EthSetTokenInt64( packetHandle, "eth", "destination", dstMacId ); if (EthInitProtocol( packetHandle, "udp" ) == 0) { // set protocol fields EthSetTokenInt( packetHandle, "ipv4", "source", 0xC0A80001 ); // 192.168.0.1 EthSetTokenInt( packetHandle, "ipv4", "destination", 0xFFFFFFFF ); // 255.255.255.255 EthSetTokenInt( packetHandle, "udp", "source", 23 ); EthSetTokenInt( packetHandle, "udp", "destination", 23 ); // set UDP payload EthResizeToken( packetHandle, "udp", "data", 5*8 /*bits*/ ); EthSetTokenData( packetHandle, "udp", "data", 5, "Hello" ); // Complete and send packet EthCompletePacket( packetHandle ); EthOutputPacket( packetHandle ); } // release packet EthReleasePacket( packetHandle );}else{ EthGetLastErrorText( elCount(error), error ); write("Error: %s", error );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
