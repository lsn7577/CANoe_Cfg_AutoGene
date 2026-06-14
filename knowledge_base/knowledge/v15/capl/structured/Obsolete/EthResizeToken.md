# EthResizeToken

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket::protocol::ResizeData |  |  |  |  |
|---|---|---|---|---|
| Note The function can only be used with resizable tokens. These are i.g. the "header" and "data" tokens. If a token is not resizable the error code 46-0125 is returned. |  |  |  |  |
| Function Syntax | long EthResizeToken( long packet, char protocolDesignator[], char tokenDesignator[], long newBitLength ); |  |  |  |
| Function | The function sets the length of a token. In case the token length is increased by full bytes, the additional bytes are initialized with 0. |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| protocolDesignator name of the protocol, e.g. "ipv4" |  |  |  |  |
| tokenDesignator name of the token, e.g. "source" |  |  |  |  |
| newBitLength new length of the token in bits |  |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example see example of EthInitPacket |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
