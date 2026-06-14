# DoIP_SetVehicleInterface

> Category: `Obsolete` | Type: `notes`

| Deprecated Function This function is replaced by DoIP_SetVehicleAdapter. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void DoIP_SetVehicleInterface( char interface[]) |  |  |  |
| Function | Sets the network interface to be used by the DoIP layer. This function must be called in on preStart. |  |  |  |
| Parameters | interface The name of the network interface. |  |  |  |
| Return Values | — |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.1 SP4 - 8.1 SP3 | — | — | • |  |
| Example // Set the network interfacechar buffer[256];DiagGetCommParameter( "DoIP.VEHICLE_Interface", 0, buffer, elcount( buffer));DoIP_SetVehicleInterface( buffer); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
