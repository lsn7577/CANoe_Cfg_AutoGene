# ISO11783 Node Layer

> Category: `ISO11783` | Type: `notes`

## Description

Access Environment Variables

Callback Functions

File Server

Network Relevant Functions

Node Control

Object Pool API

Other Functions

Process Data API

Send and Receive

Working Set Master

ISO11783 Node Layer Error Codes | ISO11783 Node Layer Error Codes: Process Data API

| ISO11783 NL To use the CAPL functions the node layer ISO11783DLL.dll must be included. You can include the node layer by using the configuration dialog of the node on page Components or via the node attribute NodeLayerModules in the database. |
|---|

| Access Environment Variables Callback Functions File Server Network Relevant Functions Node Control | Object Pool API Other Functions Process Data API Send and Receive Working Set Master |
|---|---|

| Functions | Short Description |
|---|---|
| Iso11783GetEnvDbl | Returns the value of an environment variable of type double. |
| Iso11783GetEnvInt | Returns the value of an integer environment variable. |
| Iso11783SetEnvDbl | Sets the value of an environment variable of type double. |
| Iso11783SetEnvInt | Sets the value of an integer environment variable. |

| Functions | Short Description |
|---|---|
| Iso11783AppAddrClaimed | Indicates that Address Claiming was performed successfully. |
| Iso11783AppCmdAddrIndication | Indicates that a new address has been assigned to a control device. |
| Iso11783AppErrorIndication | Indicates that errors have occurred. |
| Iso11783AppNmtIndication | Is called when an ECU claims an address or an ECU loses its address. |
| Iso11783AppRequestIndication | Indicates that the "OnRequest" parameter group has been received. |
| Iso11783AppRxIndication | Indicates that a parameter group has been received. |
| Iso11783AppTxIndication | Indicates that a PG has been sent successfully. |

| Functions | Short Description |
|---|---|
| Iso11783FSCloseFile | Closes an opened file or directory. |
| Iso11783FSGetFileInfo | Retrieves information about a file or directory. |
| Iso11783FSGetVolumeInfo | Returns information about the current volume. |
| Iso11783FSMakeAbsolutePath | Converts an relative path into an absolute path. |
| Iso11783FSMove | Moves, copies or deletes a file or directory. |
| Iso11783FSOpenFile | Opens a file or a directory. |
| Iso11783FSReadFile | Reads data from an open file and directory entries from an open directory. |
| Iso11783FSSeekFile | Moves the current write/read position. |
| Iso11783FSSetFileInfo | Sets file or directory attributes. |
| Iso11783FSSetPath | Sets the root directory for the file server functions |
| Iso11783FSWriteFile | Writes data to an open file. |

| Functions | Short Description |
|---|---|
| Iso11783EnableNameManagement | Activated or deactivated the name management of a node. |
| Iso11783GetAAC | Returns if a device is self-configuring. |
| Iso11783GetAddress | Returns the network address of a device. |
| Iso11783GetBus | Returns a bus handle. |
| Iso11783GetBusName | Returns the bus name. |
| Iso11783GetECUInstance | Returns the ECU instance of a device. |
| Iso11783GetFct | Returns the function of a device. |
| Iso11783GetFctInstance | Returns the function instance of a device. |
| Iso11783GetIG | Returns the industry group of a device. |
| Iso11783GetIN | Returns the identity number of a device. |
| Iso11783GetMC | Returns the manufacturer code of a device. |
| Iso11783GetName | Returns the name of a device. |
| Iso11783GetVS | Returns the device class of a device. |
| Iso11783GetVSInstance | Returns the device class instance of a device. |
| Iso11783MakeName | Creates a Iso11783 device name. |
| Iso11783NMTDump | Copies the current state of the network table into a buffer. |
| Iso11783SetAAC | Sets if a device is self-configuring. |
| Iso11783SetECUInstance | Sets the ECU instance of a device. |
| Iso11783SetFct | Sets the function of a device. |
| Iso11783SetFctInstance | Sets the function instance of a device. |
| Iso11783SetIG | Sets the industry group of a device. |
| Iso11783SetIN | Sets the identity number of a device. |
| Iso11783SetMC | Sets the manufacturer code of a device. |
| Iso11783SetVS | Sets the device class of a device. |
| Iso11783SetVSInstance | Sets the device class instance of a device. |
| Iso11783TableTime | Returns the time stamp of the last received "Request for Address Claim". |
| Iso11783UpdateTable | Updates the network table. |

| Functions | Short Description |
|---|---|
| Iso11783CreateECU | Sets up a logical node within a CANoe network node. |
| Iso11783DestroyECU | Deletes a logical node. |
| Iso11783ECUGoOffline | Switches the state of the ECU to offline. |
| Iso11783ECUGoOnline | Stimulates a logical ECU to log on onto the CAN bus. |
| Iso11783GetEcuState | Returns the current state of the ECU. |
| Iso11783GetNodeAddr | Returns the current address of a logical ECU. |

| Functions | Short Description |
|---|---|
| Iso11783OPActivate | Activates the object pool API. |
| Iso11783OPChangeActiveMask | Changes the active data mask. |
| Iso11783OPChangeBackgroundColor | Changes the background color of an object. |
| Iso11783OPChangeChildLocation | Moves an object. |
| Iso11783OPChangeChildPosition | Changes the absolute position of an object inside its parent object. |
| Iso11783OPChangeEndPoint | Changes the length and alignment of a line object. |
| Iso11783OPChangeFillAttribute | Changes the properties of a fill attribute object. |
| Iso11783OPChangeFontAttribute | Changes the properties of a font attribute object. |
| Iso11783OPChangeLineAttribute | Changes the properties of a line attribute object. |
| Iso11783OPChangeListItem | Changes an item in an input list object. |
| Iso11783OPChangePolygonPoint | Changes the position of a point of a polygon object. |
| Iso11783OPChangePolygonScale | Changes the size of a polygon object. |
| Iso11783OPChangePriority | Changes the priority of an alarm mask. |
| Iso11783OPChangeSize | Changes the size of an object. |
| Iso11783OPChangeSoftkeyMask | Changes the soft key mask of a data mask. |
| Iso11783OPConnectEnvVar | Connects an object from the object pool to an environment variable. |
| Iso11783OPControlAudio | Plays an acoustic signal on the Virtual Terminal. |
| Iso11783OPDeactivate | Terminates the connection to the virtual terminal. |
| Iso11783OPEnableObject | Activates or deactivates an input object. |
| Iso11783OPESC | Aborts user input on the Virtual Terminal. |
| Iso11783OPExecuteMacro | Executes a macro object. |
| Iso11783OPGetAttribute | Returns a value of an object attribute from the local object pool. |
| Iso11783OPGetNumericValue | Returns a numeric value of an object. |
| Iso11783OPGetProperty | Returns a property of the object pool API. |
| Iso11783OPGetState | Returns the state of the object pool API. |
| Iso11783OPGetStringValue | Copies a string value of an object in the object pool into a buffer. |
| Iso11783OPGetVersion | Requests the stored object pools from the Virtual Terminal. |
| Iso11783OPGetVTInfo | Returns information about the capabilities of the virtual terminal. |
| Iso11783OPLoad | Loads an object pool file (*.iop). |
| Iso11783OPLoadAuxAssignment | Loads the Preferred Auxiliary Input Assignment from an ini file. |
| Iso11783OPLoadVersion | Loads an object pool, which is stored on the Virtual Terminal. |
| Iso11783OPLock | Locks the screen updates on the Virtual Terminal. |
| Iso11783OPSave | Saves an object pool file (*.iop). |
| Iso11783OPSaveAuxAssignment | Saves the current auxiliary input assignment as Preferred Auxiliary Input Assignment in an ini file. |
| Iso11783OPSelectColorMap | Selects a color map object. |
| Iso11783OPSelectInput | Selects an input object. |
| Iso11783OPSetAttribute | Sets an attribute value of an object. |
| Iso11783OPSetAudioVolume | Sets the audio volume of the Virtual Terminal. |
| Iso11783OPSetLabel | Sets the label of an object. |
| Iso11783OPSetNumericValue | Sets the numerical value of an object. |
| Iso11783OPSetProperty | Sets a property of the object pool API. |
| Iso11783OPSetStringValue | Sets the string value of an object in the object pool. |
| Iso11783OPShowObject | Shows or hides an object. |
| Iso11783OPStoreVersion | Stores the current object pool on the Virtual Terminal. |
| Callbacks | Short Description |
| Iso11783OPOnAuxiliaryInput | Is called if an Auxiliary Input Status is received and a Auxiliary Function in the object pool is assigned. |
| Iso11783OPOnError | Is called if an error occurred. |
| Iso11783OPOnESC | Is called if the user aborts an input action. |
| Iso11783OPOnIdentifyWorkingSet | Is called if the Working Set must be identified. |
| Iso11783OPOnKeyActivation | Is called if the user presses a soft key or a button. |
| Iso11783OPOnPointingEvent | Is called if the user clicks into the data mask. |
| Iso11783OPOnResponse | Is called if a response from the virtual terminal is received. |
| Iso11783OPOnSelectInput | Is called if an input object is selected. |
| Iso11783OPOnStateChange | Is called on state change of the object pool API. |
| Iso11783OPOnValueChange | Is called if the value of an object has been changed. |

| Functions | Short Description |
|---|---|
| Iso11783GetLastError | Returns the last error code. |
| Iso11783GetLastErrorText | Gets the description of the last error occurred. |

| Functions | Short Description |
|---|---|
| Iso11783PDDChangeDesignator | Sends a Change Designator message with a new object designator to the Task Controller. |
| Iso11783PDDConnectEnvVar | Connects a process variable with an environment variable. |
| Iso11783PDDDelete | Deletes the process data dictionary. |
| Iso11783PDDGetLastError | Returns the last error code. |
| Iso11783PDDGetLastErrorText | Returns the last error description. |
| Iso11783PDDGetValue | Requests the value of a process variable. |
| Iso11783PDDLoadDeviceDescription | Creates a process data dictionary from a machine configuration file (XML). |
| Iso11783PDDObjectPoolDeactivate | Sends an Object-pool Deactivate message to the Task Controller and disconnects the connection to the Task Controller. |
| Iso11783PDDObjectPoolDelete | Deletes the current device description object pool and sends an Object-pool Delete message to the Task Controller. |
| Iso11783PDDSetDistance | Set the covered distance. |
| Iso11783PDDSetLogTrigger | Activates the default logging. |
| Iso11783PDDSetParameter | Changes an internal parameter of the process data API. |
| Iso11783PDDSetValue | Sets the value of a process variable. |
| Iso11783PDDUpdateDeviceDescription | Updates the current device description object pool at runtime. |
| Callbacks | Short Description |
| Iso11783PDDOnDataChanged | Is called if the value of a process variable has changed. |
| Iso11783PDDOnDefaultLogRequest | Is called if the default logging is requested by the task controller. |
| Iso11783PDDOnError | Is called if an error occurred. |
| Iso11783PDDOnIdentifyWorkingSet | Is called to determine the sender of a Working Set Master message. |
| Iso11783PDDOnPDM | Is called on receiving the PDM parameter group. |
| Iso11783PDDOnStateChanged | Is called on state change of the process data node layer. |

| Functions | Short Description |
|---|---|
| Iso11783GetRxData | Receives data of a parameter group. |
| Iso11783SetTPParam | Changes the settings of the transport protocol. |
| Iso11783TxAbort | Interrupts a parameter group transmission. |
| Iso11783TxReqPG | Sends a parameter group. |

| Functions | Short Description |
|---|---|
| Iso11783GetWSMAddr | Returns the address of the Working Set Master. |
| Iso11783GetWSMaster | Returns the address of the Working Set Master. |
| Iso11783SetWSMAddr | Set the address of a Working Set Master. |

| Version 15© Vector Informatik GmbH |
|---|
