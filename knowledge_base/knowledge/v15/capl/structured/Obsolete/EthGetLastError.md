# EthGetLastError

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: — |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthGetLastError( void ) |  |  |  |
| Function | Returns the error code of the last called Eth... function. |  |  |  |
| Parameters | — |  |  |  |
| Return Values | error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example CHAR error[100];LONG value;LONG packetHandle;value = EthGetTokenInt( packetHandle, "eth", "type" );if (EthGetLastError() == 0){ write("Ethernet Type is 0x%x", value );}else{ EthGetLastErrorText( elCount(error), error ); write("Error: %s", error );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
