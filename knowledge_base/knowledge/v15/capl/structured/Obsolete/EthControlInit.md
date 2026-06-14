# EthControlInit

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: — |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthControlInit(); |  |  |  |
| long EthControlInit( char protocolDesignator[] ); |  |  |  |  |
| Function | This function initializes the Ethernet Interaction Layer. The function call is only possible in on preStart. Then the Ethernet Interaction Layer has to be started with EthControlStart. If it is not called, the Ethernet Interaction Layer automatically starts with the properties defined in the node attributes. |  |  |  |
| Parameters | protocolDesignator protocol, which should be used with the IL - use IPv4 address (other values are not supported yet) |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
