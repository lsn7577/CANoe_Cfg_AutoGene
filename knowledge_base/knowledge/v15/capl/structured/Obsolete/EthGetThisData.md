# EthGetThisData

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket::GetData |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthGetThisData( long offset, long bufferSize, byte buffer[] ); |  |  |  |
| long EthGetThisData( long offset, long bufferSize, char buffer[] ); |  |  |  |  |
| long EthGetThisData( long offset, long bufferSize, struct* buffer ); |  |  |  |  |
| Function | The function gets the returned data. It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. It depends on the callback function, which part of the packet data is accessed by the function: Callback of EthReceiveRawPacket: The function handles the raw Ethernet packet data. The offset 0 is the beginning of the Ethernet packet. Callback of EthReceivePacket: The function handles the payload data of the highest interpretable protocol, i.e. in an UDP packet the functions handles the payload data of the UDP protocol. |  |  |  |
| Parameters | offset byte offset relative to the beginning of a data packet or the payload (see description above) |  |  |  |
| bufferSize number of requested bytes |  |  |  |  |
| buffer buffer in which the requested data are copied |  |  |  |  |
| Return Values | number of copied data bytes |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example Node System - PreStart in CAPL Browser on preStart{ EthReceiveRawPacket( "OnEthRawPacket");} Node Callback Function in CAPL Browser void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength){ BYTE dstMac[6]; if (EthGetThisData( 0, 6, dstMac) == 6) { write( "Destination %.2x:%.2x:%.2x:%.2x:%.2x:%.2x", dstMac[0], dstMac[1], dstMac[2], dstMac[3], dstMac[4], dstMac[5] ); }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
