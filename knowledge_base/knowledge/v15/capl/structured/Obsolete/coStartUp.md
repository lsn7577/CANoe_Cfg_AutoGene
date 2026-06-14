# coStartUp

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void coStartUp( dword nodeId, dword errCode[] ); |  |  |  |
| Function | Starts the CANopen® communication of the node. Note If no object 1200h is found at start up, the default SDO server (according to DS301) is created. Furthermore all default SDO clients are created When no objects of the range 1280h..128Fh are found. The start procedure occurs according to the specifications in the object dictionary. If the node is configured as NMT master (Bit 0 in 1F80 set) and if additional nodes are assigned to this NMT master, then these are started automatically (depending on the configuration). If the node was able to send its boot-up message, then it changes automatically to the state pre-operational. Only after this function has been executed successfully it is possible to access the object dictionary of this node via the network. The event function coOnNodeChangedState is called several times during the start procedure. Note After the call of this function, the node needs some time in order to start and be initialized completely. Therefore, it is recommended not to call CAPL functions before the event function coOnConfigReady was called with the event type 1 or 4! Otherwise the completeness and consistency of the data cannot be guaranteed. If the node is configured as NMT master, then prior the call of coOnConfigReady with the event type 1 a call with the event type 4 will occur. | Note If no object 1200h is found at start up, the default SDO server (according to DS301) is created. Furthermore all default SDO clients are created When no objects of the range 1280h..128Fh are found. | Note After the call of this function, the node needs some time in order to start and be initialized completely. Therefore, it is recommended not to call CAPL functions before the event function coOnConfigReady was called with the event type 1 or 4! Otherwise the completeness and consistency of the data cannot be guaranteed. If the node is configured as NMT master, then prior the call of coOnConfigReady with the event type 1 a call with the event type 4 will occur. |  |
| Note If no object 1200h is found at start up, the default SDO server (according to DS301) is created. Furthermore all default SDO clients are created When no objects of the range 1280h..128Fh are found. |  |  |  |  |
| Note After the call of this function, the node needs some time in order to start and be initialized completely. Therefore, it is recommended not to call CAPL functions before the event function coOnConfigReady was called with the event type 1 or 4! Otherwise the completeness and consistency of the data cannot be guaranteed. If the node is configured as NMT master, then prior the call of coOnConfigReady with the event type 1 a call with the event type 4 will occur. |  |  |  |  |
| Parameters | nodeId Node-ID that should be used by the node |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 6.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];coStartUp( 1, errCode );if (errCode[0] == 0) { write( "StartUp node" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
