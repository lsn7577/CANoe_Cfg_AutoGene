# EthIsPacketValid

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket::HasProtocolError |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthIsPacketValid( long packet ); |  |  |  |
| Function | The function checks, if a received packet has a protocol error. Packets with a protocol error are marked with an error icon in the Trace Window. |  |  |  |
| Parameters | packet handle of a packet that should be checked |  |  |  |
| Return Values | 0: packet is valid !0: packet has protocol errors |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.5-12.0 | Ethernet | — | • |  |
| Example Node System - PreStart in CAPL Browser on preStart{ EthReceivePacket( "OnEthPacket");} Node Callback Function in CAPL Browser void OnEthPacket( LONG channel, LONG dir, LONG packet ){ if (EthIsPacketValid( packet ) != 0) { write( "Receive packet with protocol error" ); }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
