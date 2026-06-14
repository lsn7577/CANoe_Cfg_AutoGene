# EthGetTokenSignalValue

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: — |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | double EthGetTokenSignalValue( long packet, dbSignal signal ); // form 1 |  |  |  |
| double EthGetTokenSignalValue( long packet, dbSignal signal, dword index); // form 2 |  |  |  |  |
| Function | Both functions assume that the packet’s payload is described in the database. They read the signal’s value of the packet’s payload. Form 2 assumes the passed signal is the first element of an array. The value will be read from the element’s position. Note The caller must check itself if the packet’s payload is described by the signal’s database frame. | Note The caller must check itself if the packet’s payload is described by the signal’s database frame. |  |  |
| Note The caller must check itself if the packet’s payload is described by the signal’s database frame. |  |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| signal signal name from databaseThe signal must be assigned to the node as Tx signal. |  |  |  |  |
| index zero based index of element |  |  |  |  |
| Return Values | Physical value |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.1 SP2-12.0 | Ethernet | — | • |  |
| Example on preStart{ EthReceivePacket( "OnEthPacket");}void OnEthPacket( LONG channel, LONG dir, LONG packet ){ DOUBLE coolantTemperature; if (EthGetTokenInt( packet, "udp", "destination" ) == 23) //this example assumes that a udp payload with destination port 23 is described by the database frame EngineInfo { coolantTemperature = EthGetTokenSignalValue( packet, EngineInfo::CoolantTemperature ); if (EthGetLastError() == 0) { write("CoolantTemperature is %f", coolantTemperature); } }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
