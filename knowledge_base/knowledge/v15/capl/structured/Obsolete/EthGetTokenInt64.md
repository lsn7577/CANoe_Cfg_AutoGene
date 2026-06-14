# EthGetTokenInt64

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket.<protocol>.<field> |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | int64 EthGetTokenInt64( long packet, char protocolDesignator[], char tokenDesignator[] ); // form 1 |  |  |  |
| int64 EthGetTokenInt64( long packet, char protocolDesignatorl[], char tokenDesignator[], long byteOffset, long length, long networkByteOrder ); // form 2 |  |  |  |  |
| Function | The function requests the integer value of a token. Form 2 with byte offset returns a part of the token data as integer. |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| protocolDesignator name of the protocol, e.g. "ipv4" |  |  |  |  |
| tokenDesignator name of the token, e.g. "source" |  |  |  |  |
| byteOffset offset from the beginning of the token in byte |  |  |  |  |
| length length of the integer value, up to 8 byte |  |  |  |  |
| networkByteOrder 0: INTEL (little-endian) 1: MOTOROLA (big-endian) |  |  |  |  |
| Return Values | integer value of the token or 0 With EthGetLastError you can check if the function has been processed successfully. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.6 SP3-12.0 | Ethernet | — | • |  |
| Example Node System - PreStart in CAPL Browser on preStart{ EthReceivePacket( "OnEthPacket" );} Node Callback Function in CAPL Browser void OnEthPacket( LONG channel, LONG dir, LONG packetHandle ){ INT64 destPort; CHAR error[100]; // get destination port of the received packet destPort = EthGetTokenInt64( packetHandle, "udp", "destination" ); if (EthGetLastError() == 0) { // do something with destPort } else { EthGetLastErrorText( elCount(error), error ); write("Error: %s", error ); }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
