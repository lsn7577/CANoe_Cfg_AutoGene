# EthGetTokenLengthBit

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: ethernetPacket.<protocol>.<field>.bitLength |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthGetTokenLengthBit( long packet, char protocolDesignator[], char tokenDesignator[] ); |  |  |  |
| Function | The function returns the length of a token in bit. |  |  |  |
| Parameters | packet handle of a packet that has been created with EthInitPacket |  |  |  |
| protocolDesignator name of the protocol, e.g. "ipv4" |  |  |  |  |
| tokenDesignator name of the token, e.g. "source" |  |  |  |  |
| Return Values | length of the token in bit With EthGetLastError you can check if the function has been processed successfully. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.5-12.0 | Ethernet | — | • |  |
| Example LONG packet = 0;LONG len = 0;CHAR error[100];packet = EthInitPacket( "udp" );len = EthGetTokenLengthBit( packet, "udp", "source" ); // = 32if (EthGetLastError() == 0){ // do something with len}else{ EthGetLastErrorText( elCount(error), error ); write("Error: %s", error );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
