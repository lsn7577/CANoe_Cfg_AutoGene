# EthGetThisMotorolaValue64

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket.QWord |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthGetThisMotorolaValue64( long offset ); |  |  |  |
| Function | This function reads the data of a received packet in Motorola format. It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. It depends on the callback function, which part of the packet data is accessed by the function: Callback of EthReceiveRawPacket: The function handles the raw Ethernet packet data. The offset 0 is the beginning of the Ethernet packet. Callback of EthReceivePacket: The function handles the payload data of the highest interpretable protocol, i.e. in an UDP packet the functions handles the payload data of the UDP protocol. |  |  |  |
| Parameters | offset byte offset relative to the beginning of a data packet or the payload (see description above) |  |  |  |
| Return Values | read value |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength ){ switch(EthGetThisMotorolaValue64( 14 )) { case 1: write( "Value 1" ); break; case 2: write( "Value 2" ); break; }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
