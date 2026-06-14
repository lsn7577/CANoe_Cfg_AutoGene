# EthAddToken

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket::protocol::optional-structure::Init |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthAddToken( long packet, char protocolDesignator[], char tokenDesignator[] ); |  |  |  |
| Function | The function adds an additional token at the end of a protocol header or at a specific position (for details see protocol help). |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| protocolDesignator name of the protocol, e.g. "dhcpv4" |  |  |  |  |
| tokenDesignator name of the token, e.g. "option1" |  |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.5-12.0 | Ethernet | — | • |  |
| Example LONG packetHandle;BYTE snameSize = 64;BYTE fileSize = 128;BYTE data[4];// create packetpacketHandle = EthInitPacket( "ipv4" );// init dhcpv4 protocolEthInitProtocol( packetHandle, "dhcpv4" );// add tokensEthAddToken( packetHandle, "dhcpv4", "serverName" );EthAddToken( packetHandle, "dhcpv4", "file" );EthAddToken( packetHandle, "dhcpv4", "magicCookie" );EthAddToken(packetHandle, "dhcpv4", "option53" ) ;EthAddToken( packetHandle, "dhcpv4", "option55" ) ;EthAddToken( packetHandle, "dhcpv4", "option50" ) ;EthAddToken( packetHandle, "dhcpv4", "option0" ) ;// set value of option 53data[0] = 3;EthSetTokenData( packetHandle, "dhcpv4", "option55.data", 1, data );// set IP address of option 55data[0] = 10;data[1] = 15;data[2] = 16;data[3] = 17;EthSetTokenData( packetHandle, "dhcpv4", "option50.data", 4, data );// complete and send packetEthCompletePacket( packetHandle );EthOutputPacket( packetHandle );// remove a tokenEthRemoveToken( packetHandle, "dhcpv4", "option50" ) ;// complete and send packet againEthCompletePacket( packetHandle );EthOutputPacket( packetHandle );// release packetEthReleasePacket( packetHandle ); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
