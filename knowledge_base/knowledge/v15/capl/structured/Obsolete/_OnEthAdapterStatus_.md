# <OnEthAdapterStatus>

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: on ethernetStatus |  |  |  |  |
|---|---|---|---|---|
| Note This callback function must be implemented in the CAPL program by the user. |  |  |  |  |
| Function Syntax | void <OnEthAdapterStatus>( long channel, long status); |  |  |  |
| Function | This callback function is called when the state of the Ethernet adapter has changed. |  |  |  |
| Parameters | channel Ethernet channel number of the adapter that has been changed |  |  |  |
| status new state of the adapter 0: unknown state 1: not connected 2: connected |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example OnEthAdapterStatus( LONG channel, LONG status){ switch(status) { case 1: // adapter disconnected write("ETH%d disconnected", channel ); break; case 2: // adapter connected write("ETH%d connected", channel ); break; default: break; }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
