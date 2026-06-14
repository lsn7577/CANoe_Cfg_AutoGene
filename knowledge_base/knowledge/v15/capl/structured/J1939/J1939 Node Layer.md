# J1939 Node Layer

> Category: `J1939` | Type: `notes`

## Description

Access Environment Variables

Callback Functions

Network Relevant Functions

Node Control

Other Functions

Send and Receive

Working Set Master

Error Codes

| J1939 Only available with J1939. To use the CAPL functions the node layer J1939_NL.DLL must be included. You can include the node layer by using the configuration dialog of the node on page Components or via the node attribute NodeLayerModules in the database. |
|---|

| Access Environment Variables Callback Functions Network Relevant Functions Node Control | Other Functions Send and Receive Working Set Master |
|---|---|

| Function | Short Description |
|---|---|
| J1939GetEnvDbl | Returns the value of an environment variable of type double. |
| J1939GetEnvInt | Returns the value of an integer environment variable. |
| J1939SetEnvDbl | Sets the value of an environment variable of type double. |
| J1939SetEnvInt | Sets the value of an integer environment variable. |

| Function | Short Description |
|---|---|
| J1939AppAddrClaimed | Indicates that Address Claiming was performed successfully. |
| J1939AppCmdAddrIndication | Indicates that a new address has been assigned to a control device. |
| J1939AppErrorIndication | Indicates that errors have occurred. |
| J1939AppNmtIndication | Is called when an ECU claims an address or an ECU loses its address. |
| J1939AppRequestIndication | Indicates that the "OnRequest" parameter group has been received. |
| J1939AppRxIndication | Indicates that a parameter group has been received. |
| J1939AppTxIndication | Indicates that a PG has been sent successfully. |

| Function | Short Description |
|---|---|
| J1939EnableNameManagement | Activated or deactivated the name management of a node. |
| J1939GetAAC | Returns if a device is self-configuring. |
| J1939GetAddress | Returns the network address of a device. |
| J1939GetBus | Returns a bus handle. |
| J1939GetBusName | Returns the bus name. |
| J1939GetECUInstance | Returns the ECU instance of a device. |
| J1939GetFct | Returns the function of a device. |
| J1939GetFctInstance | Returns the function instance of a device. |
| J1939GetIG | Returns the industry group of a device. |
| J1939GetIN | Returns the identity number of a device. |
| J1939GetMC | Returns the manufacturer code of a device. |
| J1939GetName | Returns the name of a device. |
| J1939GetVS | Returns the device class of a device. |
| J1939GetVSInstance | Returns the device class instance of a device. |
| J1939MakeName | Creates a J1939 device name. |
| J1939NMTDump | Copies the current state of the network table into a buffer. |
| J1939SetAAC | Sets if a device is self-configuring. |
| J1939SetECUInstance | Sets the ECU instance of a device. |
| J1939SetFct | Sets the function of a device. |
| J1939SetFctInstance | Sets the function instance of a device. |
| J1939SetIG | Sets the industry group of a device. |
| J1939SetIN | Sets the identity number of a device. |
| J1939SetMC | Sets the manufacturer code of a device. |
| J1939SetVS | Sets the device class of a device. |
| J1939SetVSInstance | Sets the device class instance of a device. |
| J1939TableTime | Returns the time stamp of the last received "Request for Address Claim". |
| J1939UpdateTable | Updates the network table. |

| Function | Short Description |
|---|---|
| J1939CreateECU | Sets up a logical node within a CANoe network node. |
| J1939DestroyECU | Deletes a logical node. |
| J1939ECUGoOffline | Switches the state of the ECU to offline. |
| J1939ECUGoOnline | Stimulates a logical ECU to log on onto the CAN bus. |
| J1939GetEcuState | Returns the current state of the ECU. |
| J1939GetNodeAddr | Returns the current address of a logical ECU. |

| Function | Short Description |
|---|---|
| J1939GetLastError | Returns the last error code. |
| J1939GetLastErrorText | Gets the description of the last error occurred. |

| Function | Short Description |
|---|---|
| J1939GetRxData | Receives data of a parameter group. |
| J1939SetTPParam | Changes the settings of the transport protocol. |
| J1939TxAbort | Interrupts a parameter group transmission. |
| J1939TxReqPG | Sends a parameter group. |

| Function | Short Description |
|---|---|
| J1939GetWSMAddr | Returns the address of the Working Set Master. |
| J1939GetWSMaster | Returns the address of the Working Set Master. |
| J1939SetWSMAddr | Set the address of a Working Set Master. |

| Version 15© Vector Informatik GmbH |
|---|
