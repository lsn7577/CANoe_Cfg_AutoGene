# ISO11783 Task Controller Interaction Layer

> Category: `ISO11783` | Type: `notes`

## Description

Callback Functions

DTC Support

Node Control

Other Functions

Signal/Message Access

TC - Client Control

TC - Fault Injection

TC - Other Functions

TC - Peer Control

TC - Value Access

TCIL_ExportAllDdops

TCIL_GetDeviceParameters

TCIL_RemoveAllDdops

TCIL_AssignReceiver

Sends an Assign Receiver message to the setpoint value user device.

TCIL_AssignTransmitter

Sends an Assign Transmitter message to the setpoint value source device.

TCIL_CreatePeerControlAssignment

TCIL_RemovePeerControlAssignment

TCIL_UnassignReceiver

Sends an Unassign Receiver message to the setpoint value user device.

TCIL_UnassignTransmitter

Sends an Unassign Transmitter message to the setpoint value source device.

IL Error Codes | TC IL Functional Properties | TC IL Network Properties

| ISO11783 TC IL To use the CAPL functions the ISO11783_TC_IL.dll i.e. Task Controller Interaction Layer (TC IL) must be included. |
|---|

| Callback Functions DTC Support Node Control Other Functions Signal/Message Access | TC - Client Control TC - Fault Injection TC - Other Functions TC - Peer Control TC - Value Access |
|---|---|

| Functions | Short Description |
|---|---|
| TCIL_OnAddressViolation | Is called if an address violation is detected. |
| TCIL_OnCA | Is called from the IL when a Command Address message is received. |
| TCIL_OnChangedState | Is called if the IL has changed its state. |
| TCIL_OnError | Is called if an error has occurred. |
| TCIL_OnRequest | Is called if a request (0xEA00) is received. |
| TCIL_OnRxMessage | Is called from the IL if the IL receives the parameter group, namely before the parameter group is processed by the IL. |
| TCIL_OnTxMessage | Is called if a message was sent successfully. |
| TCIL_OnTxPrepare | Is called before a parameter group is sent. |

| Functions | Short Description |
|---|---|
| TCIL_ActivateDiagnosticsSupport | Activates or deactivates the support of ISO11783 diagnostics by the IL. |
| TCIL_ActivateDTC | Activates a diagnostics trouble code (DTC) and add it to the list of active DTCs. |
| TCIL_ClearAllDTCs | Clears the list of active DTCs as well as the list of previously active DTCs. |
| TCIL_DeactivateDTC | Deactivates a diagnostics trouble code (DTC) and removes it from the list of active DTCs. |
| TCIL_GetDTCStatus | Returns the current occurrence count of a diagnostics trouble code (DTC). |

| Functions | Short Description |
|---|---|
| TCIL_AcceptRxPG | Checks if the received parameter group is addressed to the TC IL. |
| TCIL_ControlInit | Suppress the auto-start function of the IL. |
| TCIL_ControlStart | Activate node to start Address Claiming. |
| TCIL_ControlStop | Deactivates the IL and stops sending cyclic messages. |
| TCIL_EnableAddressViolationDetection | Activates detection of address violations by other nodes. |
| TCIL_EnableNameManagement | This function activates the name management of a node. |
| TCIL_GetAddress | Returns the address that is used by the TC IL. |
| TCIL_GetState | Returns the current state of the TC IL. |
| TCIL_SetNodeProperty | Changes an internal property of the node. |

| Functions | Short Description |
|---|---|
| TCIL_GetLastError | Returns the value of the last called TC IL function. |
| TCIL_GetLastErrorText | Returns the textual description of the value of the last called TC IL function. |
| TCIL_SetVerbosity | Set verbosity for writing in Write Window. |

| Functions | Short Description |
|---|---|
| TCIL_SetMsgEvent | Sends a message immediately. |
| TCIL_SetMsgRawData | Sets the data bytes of the message. |
| TCIL_SetSignal | Sets the physical value of a signal. |
| TCIL_SetSignalRaw | Sets the raw value of a signal. |

| Functions | Short Description |
|---|---|
| TCIL_MeasurementCommandRaw TCIL_MeasurementCommandPhysical | Sends a trigger definition to the client (using the raw value). Sends a trigger definition to the client (using the physical value). |
| TCIL_RequestValueCommand | Sends the Request Value command to the client |
| TCIL_RequestVersion | Requests the Version message from the client. |
| TCIL_StartTask | Starts a task. |
| TCIL_StopTask | Stops a task. |
| TCIL_ValueAndAckCommand TCIL_ValueAndAckCommandRaw TCIL_ValueAndAckCommandPhysical | Sends the current value of a data entity to the client with Set Value and Acknowledge command. Sets the value of a data entity (using the raw value) and sends the value to the client with Set Value and Acknowledge command. Sets the value of a data entity (using the physical value) and sends the value to the client with Set Value and Acknowledge command. |
| TCIL_ValueCommand TCIL_ValueCommandRaw TCIL_ValueCommandPhysical | Sends the current value of a data entity to the client with Value command. Sets the value of a data entity (using the raw value) and sends the value to the client with Value command. Sets the value of a data entity (using the physical value) and sends the value to the client with Value command. |

| Functions | Short Description |
|---|---|
| TCIL_BlockRxMessage | Prevents processing of a received message by the Interaction Layer. |
| TCIL_BlockTxMessage | Prevents transmitting of a message generated by the interaction layer. |
| TCIL_DelayRxMessage | Delays processing of a received message by the interaction layer. |
| TCIL_ManipulateMessage | Modifies the content of a message generated and sent by the interaction layer. |
| TCIL_ResetAllBlockedRxMessages | Resets the changes of all TCIL_BlockRxMessage calls. |
| TCIL_ResetAllBlockedTxMessages | Resets the changes of all TCIL_BlockTxMessage calls. |
| TCIL_ResetAllDelayedRxMessage | Resets the changes of all TCIL_DelayRxMessage calls. |
| TCIL_ResetAllManipulatedMessages | Resets the changes of all TCIL_ManipulateMessage calls. |
| TCIL_ResetBlockedRxMessage | Resets the change of a single TCIL_BlockRxMessage call. |
| TCIL_ResetBlockedTxMessage | Resets the change of a single TCIL_BlockTxMessage call. |
| TCIL_ResetDelayedRxMessage | Resets the change of a single TCIL_DelayRxMessage call. |
| TCIL_ResetManipulatedMessage | Resets the change of a single TCIL_ManipulateMessage call. |
| TCIL_ResetResponseContent | Resets the modification of TCIL_SetResponseContent. |
| TCIL_ResetTCStatus | Resets the modification of TCIL_SetTCStatus. |
| TCIL_SetResponseContent | Changes the content of the next TC response. |
| TCIL_SetTCStatus | Changes the content and cycle time of the TC Status message. |

| Functions | Short Description |
|---|---|
| TCIL_ConnectSysVarWithDataEntity | Connects a data entity to a system variable. |
| TCIL_ConnectSysVarWithSection | Connects a single section state to a system variable. |
| TCIL_ExportAllDdops | Exports the device descriptor object pools of all Task Controller clients into a file. |
| TCIL_ExportDdop | Exports the device descriptor object pool into a file. |
| TCIL_GetDesignator | Returns the designator of DeviceProcessData (DPD) or DeviceProperty (DPT). |
| TCIL_GetDeviceParameters | Returns parameters of the client device which are contained in the Device XML element (DVC) of the device description. |
| TCIL_GetValuePresentationData | Returns all properties (id, offset, scale, numberDecimals, unitDesignator) of the ValuePresentation object. |
| TCIL_MakeDdopAvailable | Enables a device descriptor object pool (DDOP) to be loaded by Object-pool Activate message. |
| TCIL_RemoveAllDdops | Removes the device descriptor object pools of all Task Controller clients. |

| Functions | Short Description |
|---|---|
| TCIL_AssignReceiver | Sends an Assign Receiver message to the setpoint value user device. |
| TCIL_AssignTransmitter | Sends an Assign Transmitter message to the setpoint value source device. |
| TCIL_CreatePeerControlAssignment | Creates an assignment of a settable process data object to a setpoint value source. |
| TCIL_RemovePeerControlAssignment | Removes an assignment of a settable process data object to a setpoint value source. |
| TCIL_UnassignReceiver | Sends an Unassign Receiver message to the setpoint value user device. |
| TCIL_UnassignTransmitter | Sends an Unassign Transmitter message to the setpoint value source device. |

| Functions | Short Description |
|---|---|
| TCIL_GetSectionState | Returns the current state of a single section. |
| TCIL_GetValueRaw TCIL_GetValuePhysical | Returns the current raw value of a data entity. Returns the current physical value of a data entity. |
| TCIL_SetSectionState | Sets the state of a single section without sending any command. |
| TCIL_SetValueRaw TCIL_SetValuePhysical | Sets the value of a data entity without sending any command (using the raw value). Sets the value of a data entity without sending any command (using the physical value). |

| Version 15© Vector Informatik GmbH |
|---|
