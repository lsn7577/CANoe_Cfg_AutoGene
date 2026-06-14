# CANopen Node Layer Functions

> Category: `Obsolete` | Type: `notes`

## Description

All functions that the node layer makes available begin with the prefix co....

Event functions that are called by the node layer and that must be filled with functionality by the user begin with coOn.... These functions must be defined by the user in the CAPL program. Here the function name and the signature must be adhered precisely. If an event function is not defined, the node layer outputs a warning in the write window at measurement start.

—

coTfsGetCANid

coTfsShowEmergenciesInReport

coTfsShowSdoAbortsInReport

coTfsUseCANid

coTfsUseNodeId

| Note To use the CAPL functions the node layer CANopenNL.dll must be included. You can include the node layer by using the configuration dialog of the node on page Components or via the node attribute NodeLayerModules in the database. |
|---|

| Quick Access |  |  |
|---|---|---|
| Access to the object dictionary of other nodes | Access to the local object dictionary | Generate the local object dictionary |
| Data access in event functions | General | Layer Setting Services |
| Network Management | Node Control | PDO Control |
| Event functions | Test Feature Set | — |

| Functions | Short Description |
|---|---|
| coDownload | Writes an entry into the object dictionary of another node by using the SDO download. |
| coDownloadExpedited | Writes an entry into the object dictionary of another node by using the expedited SDO download. |
| coSetBlockSize | Sets the block size used for SDO block transfers. |
| coSetSDOTimeout | Sets the time-out value for an abort of a SDO transfer. |
| coUpload | Reads an entry from the object dictionary of another node by using the SDO upload. |

| Functions | Short Description |
|---|---|
| coODAbortTransfer | Aborts a SDO transfer. |
| coODConnectEnvVar | Connects an object with an environment variable. |
| coODDisconnectEnvVar | Deletes the connection of an object to an environment variable. |
| coODDownloadResponse | Confirms a SDO download transfer. |
| coODGetBitSize | Returns the size of an object in bits. |
| coODGetData | Returns the data of an object. |
| coODGetFloat | Returns the floating point value of an object. |
| coODGetSigned | Returns the value of an object of type signed. |
| coODGetSize | Returns the size of an object in bytes. |
| coODGetType | Returns the data type of an object. |
| coODGetUnsigned | Returns the value of an object of type unsigned. |
| coODSetData | Sets the data of an object. |
| coODSetFloat | Sets the floating point value of an object. |
| coODSetSigned | Sets the value of an object of type signed. |
| coODSetUnsigned | Sets the value of an object of type unsigned. |
| coODUploadResponse | Confirms a SDO upload transfer. |

| Functions | Short Description |
|---|---|
| coODCreate | Creates a new object in the local object dictionary of the node. |
| coODCreateArray | Creates a new array object in the local object dictionary. |
| coODCreateFloat | Creates a new object of type float. |
| coODCreateFromFile | Creates the object dictionary by reading an EDS Electronic Data Sheet or DCF Device Configuration File file. |
| coODCreateSigned | Creates a new object of type signed. |
| coODCreateUnsigned | Creates a new object of type unsigned. |

| Functions | Short Description |
|---|---|
| coThisGetData | Returns the data of an object. |
| coThisGetFloat | Returns a floating point value of an object. |
| coThisGetSigned | Returns the value with leading sign of an object. |
| coThisGetSize | Returns the size of the data of a SDO transfer. |
| coThisGetUnsigned | Returns the value without leading sign of an object. |

| Functions | Short Description |
|---|---|
| coGetLastError | Returns the error code and text of the last function call. |
| coGetNodeLabel | Returns the label of the node. |
| coGetValue | Returns the current value of an environment variable of type integer. |
| coGetVersionInfo | Returns the current version number of the used node layer. |
| coPutValue | Sets the value of an environment variable of type integer. |
| coSetNodeLabel | Sets the label of the node. |
| coSetOutputLevel | Sets the output level of the used node layer. |

| Functions | Short Description |
|---|---|
| coLssConfigNodeId | The LSS master configures the node-ID of a LSS slave. |
| coLssIdentNonConfigSlave | The LSS master commands all LSS slaves whose node-ID is not configured (0xFF) to identify themselves. |
| coLssIdentRemoteSlave | The LSS master commands all LSS slaves whose LSS address matches to the transmitted LSS address parameters to identify themselves. |
| coLssInqNodeId | Causes the determination of the node-ID of a LSS slave. |
| coLssInqProdCode | Causes the determination of the product code of a LSS slave. |
| coLssInqRevNo | Causes the determination of the revision number of a LSS slave. |
| coLssInqSerialNo | Causes the determination of the serial number of a LSS slave. |
| coLssInqVendorId | Causes the determination of the vendor-ID of a LSS slave. |
| coLssStoreConfig | The configured parameters are written into non-volatile memory with this service. |
| coLssSwitchModeGlob | Sets all LSS slaves to the configuration mode or leaving of the mode. |
| coLssSwitchModeSel | Puts a single LSS slave into the configuration mode. |

| Functions | Short Description |
|---|---|
| coGetNMTState | Returns the state of a node on the network. |
| coSetNMTState | Sets the state of a node on the network. |

| Functions | Short Description |
|---|---|
| coAllowStart | Allows several communication state changes during the start procedure of a CANopen® node. |
| coEmergency | Activates or deactivates an emergency error code. |
| coGetLocalState | Returns the current communication state of the node. |
| coGetNodeId | Returns the node-ID. |
| coSetLocalState | Sets the communication state of the node. |
| coSetOperatingMode | Sets the operating mode of the node. |
| coShutDown | Stops the CANopen® communication of the node. |
| coStartUp | Starts the CANopen® communication of the node. |

| Functions | Short Description |
|---|---|
| coTriggerTPDO | Triggers the immediate transmission of a TPDO. |

| Functions | Short Description |
|---|---|
| coOnBootUp | This function is called if a boot-up message was registered on the bus. |
| coOnConfigReady | The function informs the user about the current state of the configuration process. |
| coOnDownloadIndication | This function is called if a SDO download is executed. |
| coOnDownloadResponse | This function is called if the response to a SDO download was received. |
| coOnUploadIndication | This function is called if a SDO upload is executed. |
| coOnUploadResponse | This function is called when the response to a SDO upload was received. |
| coOnNodeChangedState | This function is called if the state of the node changes. |
| coOnRPDOMissing | The function is called if an event timer of a RPDO is activated and the PDO is not received in the defined time. |
| coOnLssEvent | This function is called if the response of a LSS command was received. |
| coOnEmergency | This function is called if an emergency message was received. |
| coOnError | This function is called if an error occurs. |

| Functions | Short Description |
|---|---|
| coTfsGetCANid | This function returns the internally-stored CAN-ID that is used for the simplified test functions. |
| coTfsShowEmergenciesInReport | Allows the report of emergency code in the test protocol. |
| coTfsShowSdoAbortsInReport | Allows the report of SDO aborts in the test protocol. |
| coTfsUseCANid | Transmits the internally-stored CAN label to the simplified test functions insofar as it is supported. |
| coTfsUseNodeId | This function instructs the node layer, for functions which accept both the node-ID and the CAN-ID as parameter, to use the node-ID. |

| Version 15© Vector Informatik GmbH |
|---|
