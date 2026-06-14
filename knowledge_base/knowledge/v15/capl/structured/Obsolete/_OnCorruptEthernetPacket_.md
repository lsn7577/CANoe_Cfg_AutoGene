# <OnCorruptEthernetPacket>

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: on ethernetErrorPacket |  |  |  |  |
|---|---|---|---|---|
| Note This callback function must be implemented in the CAPL program by the user to use the function EthReceiveRxError. |  |  |  |  |
| Function Syntax | void <OnCorruptEthernetPacket>( long channel, long errorCode, long packetLength ); |  |  |  |
| Function | This callback function is called when a corrupt Ethernet packet is received. Within this callback function the following functions can be used to retrieve the received packet data: EthGetThisData EthGetThisTimeNS EthGetThisValue8 EthGetThisValue16 EthGetThisValue32 EthGetThisValue64 EthGetThisMotorolaValue16 EthGetThisMotorolaValue32 EthGetThisMotorolaValue64 The functions access the raw Ethernet data. Offset 0 starts at the beginning of the Ethernet header. |  |  |  |
| Parameters | channel Ethernet channel number of the adapter that has been changed. |  |  |  |
| errorCode error code to identify the error type 0x01: invalid length of the Ethernet frame 0x02: invalid CRC of the Ethernet frame 0x04: invalid data received 0x08: collision detected (half duplex mode) |  |  |  |  |
| packetLength number of bytes of the received packet (see Packet Length) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.1-12.0 | Ethernet | — | • |  |
| Example see example of EthReceiveRxError |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
