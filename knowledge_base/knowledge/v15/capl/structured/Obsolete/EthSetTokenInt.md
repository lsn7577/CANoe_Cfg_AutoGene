# EthSetTokenInt

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket Selectors: <protocol>.<field> |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthSetTokenInt( long packet, char protocolDesignatorl[], char tokenDesignator[], long value ); // form 1 |  |  |  |
| long EthSetTokenInt( long packet, char protocolDesignatorl[], char tokenDesignator[], long byteOffset, long length, long networkByteOrder, long value ); // form 2 |  |  |  |  |
| Function | The function sets the integer value of a token. Form 2 with byte offset sets a part of the token data as integer. |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| protocolDesignator name of the protocol, e.g. "ipv4" |  |  |  |  |
| tokenDesignator name of the token, e.g. "source" |  |  |  |  |
| byteOffset offset from the beginning of the token in byte |  |  |  |  |
| length length of the integer value, must be 1, 2, 3 or 4 byte |  |  |  |  |
| networkByteOrder 0: INTEL (little-endian) 1: MOTOROLA (big-endian) |  |  |  |  |
| value new integer value |  |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example see example of EthInitPacket |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
