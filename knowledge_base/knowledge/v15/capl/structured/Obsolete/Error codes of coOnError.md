# Error codes of coOnError

> Category: `Obsolete` | Type: `notes`

## Description

The error class and error codes of the function coOnError are listed in the table below. The parameters index, subIndex, nodeId and param are only valid in particular error classes.

See Also

| Error Code | Description | Output Level |
|---|---|---|
| Error Class 1, API Error The parameter param is partially valid. |  |  |
| 0x20 | Error during command execution. | 2 |
| 0x21 | A timer was required for an action and could not be allocated. | 2 |
| 0x24 | There was an attempt to use a CAN identifier that is already assigned. param contains the associated CAN identifier. | 3 |
| 0x27 | The specified node ID is not valid. | 2 |
| 0x28 | A COB-ID was received that is already used by the node itself. param contains the associated CAN identifier. | 2 |
| 0x29 | One or more default mapping entries were invalid (not mappable, wrong access type, wrong length). param contains the flawed mapping entry. | 5 |
| 0x2a | The maximum length or object number for a PDO was exceeded or the length specified in the mapping does not match the object length. param contains the flawed mapping entry and the flawed object. | 5 |
| 0x2b | A restricted identifier for a communication object was detected. The relating COB was disabled, param contains the COB index. | 5 |
| 0x2c | A received message could not be processed further since the access to the memory interface was blocked (layer 2 or SYNC message or RPDO). | 3 |
| 0x2d | An unknown command code was discovered in the command queue. | 3 |
| 0x2e | During the configuration of a slave via the configuration manager, an error occurred. param contains in the lowest-value byte (byte 0) the node-ID of the slave where the problem occurred. One of the following error codes is in byte 1:1 - the stored configuration data is not valid.2 - inconsistency in the management of the memory pages for the configuration.3 - the necessary SDO transfer for the configuration of a value could not be started.4 - an entry in the "concised" data (configuration data) appears to be inconsistent.5 - a checksum error was determined for the configuration data.7 - during the transmission of configuration data, a SDO time-out error occurred.8 - the transmission of configuration data was answered by the SDO server with an abort. (e.g. write access to an read-only object or object does not exist) | 5 |
| Error Class 2, CAN Error |  |  |
| 0x02 | The transmit queue is full. | 3 |
| Error Class 3, SDO Error The parameters index, subIndex and nodeId are valid.Error codes that are marked with [DS301] corresponds to the error codes defined in the DS301. Error codes that begin with 0xFF01xxxxx are error codes defined by Vector. |  |  |
| 0x05030000 | For a segmented transfer, the toggle bit was not switched for segments that follow one another [DS301]. | 4 |
| 0x05040000 | The SDO connection was ended by a time-out [DS301]. | 4 |
| 0x05040001 | The service ID for the SDO service started is unknown [DS301]. | 4 |
| 0x05040002 | The block size is invalid [DS301]. | 4 |
| 0x05040003 | Within a block, an invalid sequence number was used [DS301]. | 4 |
| 0x05040004 | A CRC number occurred [DS301]. | 4 |
| 0x05040005 | There is not enough memory available [DS301]. | 5 |
| 0x06010000 | The selected access type is not supported for the object [DS301]. | 5 |
| 0x06010001 | There was an attempt to read an object that can only be written [DS301]. | 7 |
| 0x06010002 | There was an attempt to write an object that can only be read [DS301]. | 7 |
| 0x06020000 | The object does not exist in the object dictionary [DS301]. | 7 |
| 0x06040041 | The object cannot be mapped in a PDO [DS301]. | 7 |
| 0x06040042 | The number and/or length of the objects to be mapped would exceed the capacity of a PDO [DS301]. | 7 |
| 0x06040043 | General incompatibility of the parameters [DS301]. | 6 |
| 0x06040047 | General internal incompatibility in the device [DS301]. | 6 |
| 0x06060000 | This access failed due to a hardware error [DS301]. | 6 |
| 0x06070010 | The data type does not fit. The length of the service parameter does not fit [DS301]. | 7 |
| 0x06070012 | The data type does not fit. The length of the service parameter is too large [DS301]. | 7 |
| 0x06070013 | The data type does not fit. The length of the service parameter is too small [DS301]. | 7 |
| 0x06090011 | The sub index does not exist [DS301]. | 7 |
| 0x06090030 | The value range of the parameter was exceeded [DS301]. | 7 |
| 0x06090031 | The value of the written parameter is too large [DS301]. | 7 |
| 0x06090032 | The value of the written parameter is too small [DS301]. | 7 |
| 0x06090036 | The maximum value is smaller than the minimum value [DS301]. | 7 |
| 0x08000000 | General error [DS301]. | 6 |
| 0x08000020 | It is not possible to transmit the data to the application or to save it there [DS301]. | 7 |
| 0x08000021 | The local control does not permit the transmission of the data to the application or its storage there [DS301]. | 7 |
| 0x08000022 | The current device state does not permit the transmission of the data to the application or its storage there [DS301]. | 7 |
| 0x08000023 | The object dictionary could not be generated or no object is available [DS301]. | 6 |
| 0xFF010024 | A SDO identifier could not be entered into the filter list. | 4 |
| 0xFF010032 | Protocol error | 4 |
| 0xFF010034 | A transfer is already running for this SDO. | 8 |
| 0xFF010035 | The SDO is no longer in the command queue (e.g. because it was deleted by a time-out). | 8 |
| 0xFF010036 | For the execution of a SDO transfer, no memory could be provided for the necessary buffer. | 5 |
| 0xFF010037 | For the execution of a SDO transfer, no length could be determined for the necessary buffer. | 5 |
| 0xFF01003A | The selected SDO cannot be used. | 6 |
| Error Class 4, Guarding Error The parameter nodeId is valid. |  |  |
| 0 | The guarding is not activated. | 7 |
| 1 | The guarding was (re) activated. This message occurs if the guarding for a node was transferred from the error state to the error-free state (temporary status error). | 7 |
| 2 | The guarding response of a node was not received within the guard time. | 8 |
| 3 | The guard response of a node was not received within the time span GuardTime t * LifeTimeFactor n. Before this event, the code 2 was reported n times. The guarding for the node thus failed. | 6 |
| 4 | The toggle bit of the slave message does not match the expected value. The master adjusts its toggle value so that this error is only triggered once. | 7 |
| 5 | The slave reported a communication status that the master did not specify. This error occurs during a local status change in the slave. The master adjusts its status value so that this error is only triggered once. | 7 |
| 6 | A heartbeat event occurred. The heartbeat time for a node entered in the heartbeat consumer table has expired without receipt of a heartbeat. | 6 |
| 9 | A life-guard error has occurred. | 6 |
| Error Class 5, Boot Error The parameter nodeId is valid. |  |  |
| 0x51 | To determine the attributes (identity object, device type, verify configuration) of the connected node, no SDO transfer could be triggered (internal error). | 4 |
| 0x52 | To determine the attributes (identity object, device type, verify configuration) of the connected node, an incorrect sub index was accessed (internal error). | 5 |
| 0x53 | To determine the attributes (identity object, device type, verify configuration) of the connected node, an incorrect sub index was accessed (internal error). | 5 |
| 0x54 | To determine the attributes (identity object, device type, verify configuration) of the connected node, an incorrect node-ID was accessed (internal error). | 5 |
| 0x55 | For the node to be configured, a time-out occurred during SDO access. | 4 |
| 0x56 | For the node to be configured, a difference occurred during a value comparison (identity object, device type). | 3 |
| 0x57 | The status machine of the master is in an error state. | 3 |
| Error Class 8, LSS Error |  |  |
| 0x02 | The LSS message could not be written in the send queue. | 4 |
| 0x21 | No timer could be allocated for the execution of the service. | 4 |
| 0x24 | The LSS message identifier could not be allocated. | 4 |
| 0x61 | The started service received no response within the time-out time. | 8 |
| 0x62 | There was an attempt to start a service while another service is already in processing. | 9 |
| 0x63 | Unexpected command specifier in the LSS response. | 5 |

| Version 15© Vector Informatik GmbH |
|---|
