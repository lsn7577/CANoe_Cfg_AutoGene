# coTriggerTPDO

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by CANopen Basic Functions. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword coTriggerTPDO( dword pdoNumber, dword errCode[] ); |  |  |  |
| Function | Generally a simulated node is used with a defined cycle time. The default value is 5 ms, but it can be changed with the function coSetOperatingMode() for each node. The cycle time also defines the reaction time on data changes of the PDOs. Consider that a decrease of the node processing time leads to a higher load of the simulated system. If it is necessary to transmit the PDO directly after the data change, this function can be used. It triggers the immediate transmission of a TPDO. The following conditions have to be fulfilled to allow the transmission of a TPDO with this function: The relating node has to be in the communication state operational. COB-ID has to be valid (TPDO enabled). The configured mapping of the TPDO is valid. The Transmission type of the TPDO has to be 254 or 255. A potentially configured inhibit time for this TPDO is not currently active. The transmission message queue is not full. Note If one of this conditions is not fulfilled, the transmission of the relating TPDO will not be triggered and the function returns with an error. | Note If one of this conditions is not fulfilled, the transmission of the relating TPDO will not be triggered and the function returns with an error. |  |  |
| Note If one of this conditions is not fulfilled, the transmission of the relating TPDO will not be triggered and the function returns with an error. |  |  |  |  |
| Parameters | pdoNumber Number of the transmitted PDO, value range 1..512 |  |  |  |
| errCode Error code buffer (is entered in index 0 of the field) |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.0-9.0 SP6 | CANopen | — | • |  |
| Example dword errCode[1];putValue(MyProcessData, 0x1234);coTriggerTPDO( 1, errCode );if (errCode[0] == 0) { write( "TPDO 1 triggered successfully" );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
