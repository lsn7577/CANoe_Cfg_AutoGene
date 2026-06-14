# <OnEthPacket>

> Category: `Obsolete` | Type: `notes`

## Description

—

See Also

| Deprecated Function Replaced by: on ethernetPacket |  |  |  |  |
|---|---|---|---|---|
| Note This callback function must be implemented in the CAPL program by the user to use the function EthReceivePacket. |  |  |  |  |
| Function Syntax | void <OnEthPacket>( long channel, long dir, long packet); |  |  |  |
| Function | The function is called when a registered Ethernet packet is received. Within this callback function the following functions can be used to retrieve the received packet data: EthGetThisData EthGetThisTimeNS EthGetThisValue8 EthGetThisValue16 EthGetThisValue32 EthGetThisValue64 EthGetThisMotorolaValue16 EthGetThisMotorolaValue32 EthGetThisMotorolaValue64 The functions access the payload of the highest interpretable protocol. Offset 0 starts at the beginning of the payload. |  |  |  |
| Parameters | channel Ethernet channel on which the packet was received |  |  |  |
| dir direction of the packet 0: Rx 1: Tx |  |  |  |  |
| packet handle of the received packet |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2 | Ethernet | — | • |  |
| Example see example of EthReceivePacket |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
