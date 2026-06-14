# EthGetTokenData

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket::protocol::field::GetData |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, char buffer[] ); |  |  |  |
| long EthGetTokenData( long packet, char protocolDesignator[], char tokenDesignatorl[], long length, byte buffer[] ): |  |  |  |  |
| long EthGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, struct bufferStruct ); |  |  |  |  |
| long EthGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, char buffer[] ); |  |  |  |  |
| long EthGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, byte buffer[] ); |  |  |  |  |
| long EthGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, struct bufferStruct ); |  |  |  |  |
| Function | The function requests the data or a part of date of a token. |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| protocolDesignator name of the protocol, e.g. "ipv4" |  |  |  |  |
| tokenDesignator name of the token, e.g. "source" |  |  |  |  |
| byteOffset offset from the beginning of the token in byte |  |  |  |  |
| length number of bytes to be copied Make sure size of destination (buffer or bufferStruct) is equal or larger than length. |  |  |  |  |
| buffer buffer in which the data are copied |  |  |  |  |
| bufferStruct struct in which the data are copied |  |  |  |  |
| Return Values | number of copied bytes or 0 With EthGetLastError you can check if the function has been processed successfully. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example Node System - PreStart in CAPL Browser on preStart{ EthReceivePacket( "OnEthPacket" );} Node Callback Function in CAPL Browser void OnEthPacket( LONG channel, LONG dir, LONG packetHandle ){ BYTE data[5]; CHAR error[100]; // get udp payload of the receive packet EthGetTokenData( packetHandle, "udp", "data", 5, data ); if (EthGetLastError() == 0) { // do something with data } else { EthGetLastErrorText( elCount(error), error ); write("Error: %s", error ); }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
