# EthGetThisFrameCheckSequence

> Category: `Obsolete` | Type: `notes`

## Description

dword EthGetThisFrameCheckSequence();

See Also

| Deprecated Function Replaced by: ethernetPacket.fcs |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword EthGetThisFrameCheckSequence(); |  |  |  |
| Function | The function returns the frame check sequence (fcs) of a received Ethernet packet. It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. |  |  |  |
| Parameters | — |  |  |  |
| Return Values | frame check sequence of the Ethernet frame |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.1-12.0 | Ethernet | — | • |  |
| Example Node System - PreStart in CAPL Browser on preStart{ BYTE emptyMacId[6] = { 0x00,0x00,0x00,0x00,0x00, 0x00}; EthReceiveRawPacket( 0x7, emptyMacId, emptyMacId, 0x0000, "OnEthRawPacket");} Node Callback Function in CAPL Browser void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength){dword fcs;fcs = EthGetThisFrameCheckSequence();write("Received packet with fcs %d", fcs );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
