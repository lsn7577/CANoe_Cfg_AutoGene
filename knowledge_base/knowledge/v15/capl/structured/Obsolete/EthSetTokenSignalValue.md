# EthSetTokenSignalValue

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: — |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthSetTokenSignalValue( long packet, dbSignal signal, double physValue ); // form 1 |  |  |  |
| long EthSetTokenSignalValue( long packet, dbSignal signal, double physValue, dword index); // form 2 |  |  |  |  |
| Function | Both functions assume that the packet’s payload is described in the database. They writes the signal’s value into the packet’s payload. Form 2 assumes the passed signal is the first element of an array. The value will be written to the element’s position. Note The caller must check itself if the packet’s payload is described by the signal’s database frame. | Note The caller must check itself if the packet’s payload is described by the signal’s database frame. |  |  |
| Note The caller must check itself if the packet’s payload is described by the signal’s database frame. |  |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| signal signal name from databaseThe signal must be assigned to the node as Tx signal. |  |  |  |  |
| physValue physical value |  |  |  |  |
| index zero based index of element |  |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.1 SP2-12.0 | Ethernet | — | • |  |
| Example LONG packetHandle;CHAR error[100];// create packetpacketHandle = EthInitPacket("udp");if (EthGetLastError() == 0){ // set protocol fields EthSetTokenInt( packetHandle, "ipv4", "source", 0xC0A80001 ); // 192.168.0.1 EthSetTokenInt( packetHandle, "ipv4", "destination", 0xFFFFFFFF ); // 255.255.255.255 EthSetTokenInt( packetHandle, "udp", "source", 23 ); EthSetTokenInt( packetHandle, "udp", "destination", 23 ); //this example assumes that a udp payload with destination port 23 is described by the database frame EngineInfo // set UDP payload EthResizeToken( packetHandle, "udp", "data", EngineInfo.DLC*8 /*bits*/ ); EthSetTokenSignalValue( packetHandle, EngineInfo::CoolantTemperature, 77.0 ); // Complete and send packet EthCompletePacket( packetHandle ); EthOutputPacket( packetHandle ); // release packet EthReleasePacket( packetHandle );}else{ EthGetLastErrorText( elCount(error), error ); write("Error: %s", error );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
