# EthCompletePacket

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket::CompletePacket |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthCompletePacket( long packet ); |  |  |  |
| Function | The function completes a packet before sending it with EthOutputPacket. It calculates the fields that are marked with CompleteProtocol in the protocol overview, e.g. checksum, lengths, etc. |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example see example of EthInitPacket |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
