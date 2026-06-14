# EthGetLastErrorText

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: — |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthGetLastErrorText( dword bufferSize, char[] buffer ); |  |  |  |
| Function | Gets the error code description of the last called Eth... function. |  |  |  |
| Parameters | bufferSize size of buffer in which the description text is copied |  |  |  |
| buffer buffer in which the description text is copied |  |  |  |  |
| Return Values | number of copied bytes |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example CHAR error[100];LONG value;LONG packetHandle;value = EthGetTokenInt( packetHandle, "eth", "type" );if (EthGetLastError() == 0){ write("Ethernet Type is 0x%x", value );}else{ EthGetLastErrorText( elCount(error), error ); write("Error: %s", error );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
