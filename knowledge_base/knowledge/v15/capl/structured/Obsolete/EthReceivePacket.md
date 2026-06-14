# EthReceivePacket

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: on ethernetPacket |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthReceivePacket( char *onPacketCallback ); |  |  |  |
| Function | Use this function to register a CAPL callback function to receive Ethernet packets. The callback has a packet handle as parameter and the functions to access the tokens can be used. The EthGetThis-functions can be used to access the payload of the highest interpretable protocol. The callback must have the following signature: void <OnEthPacket> ( long channel, long dir, long packet ) The difference to EthReceiveRawPacket is, that the callback function gets a packet handle as parameter and the EthGetThis-Functions access the payload of the highest protocol instead the raw Ethernet data. |  |  |  |
| Parameters | onPacketCallback name of CAPL callback function |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example Node System - PreStart in CAPL Browser on preStart{ EthReceivePacket( "OnEthPacket");} Node Callback Function in CAPL Browser void OnEthPacket( LONG channel, LONG dir, LONG packet ){ BYTE rx_data[100]; LONG rx_length; // get the payload of the packet rx_length = EthGetThisData( 0, elCount(rx_data), rx_data ); // do something with rx_data} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
