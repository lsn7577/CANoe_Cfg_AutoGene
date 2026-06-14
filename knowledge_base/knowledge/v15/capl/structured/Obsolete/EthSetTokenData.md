# EthSetTokenData

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket::protocol::SetData |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, char data[] ); |  |  |  |
| long EthSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, byte data[] ); |  |  |  |  |
| long EthSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, struct dataStruct ); |  |  |  |  |
| long EthSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, char data[] ); |  |  |  |  |
| long EthSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, byte data[] ); |  |  |  |  |
| long EthSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, struct dataStruct ); |  |  |  |  |
| Function | The function sets the data or a part of data of a token. It does not resize the token. Use EthResizeToken to change the length. |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| protocolDesignator name of the protocol, e.g. "ipv4" |  |  |  |  |
| tokenDesignator name of the token, e.g. "source" |  |  |  |  |
| byteOffset offset from the beginning of the token in byte |  |  |  |  |
| length number of bytes to be copied |  |  |  |  |
| data data that are copied to the token |  |  |  |  |
| dataStruct struct containing the data |  |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example see example of EthInitPacket |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
