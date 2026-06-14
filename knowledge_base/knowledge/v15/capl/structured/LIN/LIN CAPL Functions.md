# LIN CAPL Functions

> Category: `LIN` | Type: `notes`

## Description

Configuring and Controlling a Simulated LIN Master

Configuring and Controlling a Simulated LIN Slave

Configuring and Controlling Network Management

Event Procedures

Further Topics

LIN Analysis Feature Set

LIN Disturbance Feature Set

LIN Stress Feature Set

LIN Transport Layer

Selectors

Test Feature Set for LIN

Test Service Library for LIN

linConfigureResponse

linConfigureResponseRange

Checks if the network channel given by the current bus context is running in master mode.

linTransmitHeader

linUpdateResponse

linSetExpectedRespLength

Access to the data of the corresponding event is possible in event procedures through this.

The procedures are sub-divided into the following events:

linGetMeasByteBitRates

linIsBitStreamBusy

TestWaitForLinBitStreamStatus

TestWaitForLinScheduleChange

Network Hardware | Timeout Prevention | Notes to NAD | LIN Overview | Configuration: Network Hardware

| LIN Only available with option .LIN. These CAPL functions are supported by Windows and Linux. The functionality under Linux has not been fully tested yet. |
|---|

| Configuring and Controlling a Simulated LIN Master Configuring and Controlling a Simulated LIN Slave Configuring and Controlling Network Management Event Procedures Further Topics LIN Analysis Feature Set | LIN Disturbance Feature Set LIN Stress Feature Set LIN Transport Layer Selectors Test Feature Set for LIN Test Service Library for LIN |
|---|---|

| Functions | Short Description |
|---|---|
| getSignal | Gets the value of a signal. |
| linActivateCollisionResolution | Activates or deactivates the Master node’s automatic collision resolution of an event-triggered frame. |
| linActivateSlot | Reactivates a schedule table slot defined in the LIN database file. |
| linChangeSchedTable | Switches from the current schedule table to another one. |
| linCheckRespError | Queries the response_error flags of all Slave nodes defined in the LIN network. |
| linConfigureResponse | Configures a response frame of a LIN slave if no database is used. |
| linConfigureResponseRange | Configures a range of frames as response of a LIN node if no database is used. |
| linDeactivateSlot | Deactivates the specified slot of schedule table. |
| linGetMasterNode | This function returns a unique internal ID for the current LIN master node of the channel given by the current bus context. |
| linGetMasterResistorState | Returns the internal master resistor’s current state of the LIN interface hardware. |
| linIsChannelMasterMode | Checks if the network channel given by the current bus context is running in master mode. |
| linIsMasterNode | Checks if the calling node is the current LIN master node of the network given by the current bus context. |
| linRegisterSchedulerStartStopCallback | Registers a callback function which is invoked if a LIN scheduler is either started or stopped. |
| linResetMasterNode | Reverses the effect of linSetMasterNode. |
| linRunSchedTableNtimes | Switches from the current schedule table to another one, runs the table n times and returns to the initial table or to a different table. |
| linSendAsSporadic | Configures an associated frame as being ready for transmission. |
| linSetBreakLength | Changes length of break/synch symbol parts. |
| linSetChannelMasterMode | The channel specified by the current bus context can be switched to master or slave mode. |
| linSetChecksumCompatibility | Sets the checksum model of all frames that are received by a LIN 1.x node to classic. |
| linSetChecksumModel | Sets the checksum calculation model for a LIN frame. |
| linSetGlobalInterByteSpace | Changes the inter-byte space for all frame responses. |
| linSetInterByteSpace | Sets an inter-byte space for a specified frame and a specified byte filed. |
| linSetInterByteSpaces | Sets the inter-byte spaces for all data byte fields of all published frames of the calling LIN Slave node. |
| linSetInterframeSpace | Sets the minimum inter-frame space. |
| linSetInterruptingHeaderTransmits | The channel specified by the current bus context will be switched to interrupting mode. |
| linSetMasterNode | Changes the LIN master node of the channel given by the current node’s bus context and restricts sending LIN headers solely to the assigned master node. |
| linSetMasterRequestDirtyFlag | Sets the dirty flag for the LIN master request frame. |
| linSetMasterResistor | Enables or disables the internal master resistor of the LIN hardware interface. |
| linSetOEMDataInd | Sets/resets the data indication bit for a calling slave node. |
| linSetOEMSleepInd | Sets/resets the sleep indication bit for a calling slave node. |
| linSetOEMWakeupInd | Sets/resets the wake-up indication bit for a calling slave node. |
| linSetSchedulerJitter | Sets/resets the jitter mode and the jitter of the LIN hardware scheduler. |
| linSimulateETFCollision | Causes collisions for next coming header(s) of an event-triggered frame. |
| linStartScheduler | Starts the internal scheduler. |
| linStopScheduler | Stops the internal scheduler. |
| linTransmitHeader | Transmits a frame header for a specific LIN frame. |
| linUpdateResponse | Updates the response data of a specific LIN frame. |
| output | Applies frame header on the bus or reconfigures response data of LIN frame. |
| setSignal | Sets the transmitted signal to the accompanying value. |

| Functions | Short Description |
|---|---|
| getSignal | Gets the value of a signal. |
| linActivateGlobalNetworkManagement | Activates/deactivates network management for the entire LIN network. |
| linActivateResps | Reactivates all frame responses published by the calling Slave node according to the LIN database file. |
| linConfigureResponse | Configures a response frame of a LIN slave if no database is used. |
| linConfigureResponseRange | Configures a range of frames as response of a LIN slave if no database is used. |
| linDeactivateResps | Deactivates frame responses for all frames published by the calling slave node. |
| linETFSendOnSignalUpdate | Activates/deactivates the automatic responses on a certain event-triggered frame request in the case of a signal update on its associated frame(s). |
| linETFSetDirtyFlag | Sets/clears the dirty flag of an associated frame. |
| linGetBusIdleTimeout | Returns the currently set bus idle timeout. |
| linGetOEMDataInd | Queries the data indication bit of a Slave node. |
| linGetOEMSleepInd | Queries the sleep indication bit of a Slave node. |
| linGetOEMWakeupInd | Queries the wake-up indication bit of a Slave node. |
| linGetRespError | Queries the response error flag of the calling Slave node or of the Slave node. |
| linResetNAD | Resets NAD of the Slave node determined by the CAPL program context to its initial NAD. |
| linResetRespBaudrate | Resets a response baud rate for a specified frame to the master baud rate. |
| linResetSlave | Resets the NAD of the modeled Slave node. |
| linSetBusIdleTimeout | Sets a new bus idle timeout. |
| linSetExpectedRespLength | This function can be used to configure how many data bytes of the frame response will be expected on reception. |
| linSetGlobalInterByteSpace | Changes the inter-byte space for all frame responses. |
| linSetInterByteSpace | Sets an inter-byte space for a specified frame and a specified byte filed. |
| linSetInterByteSpaces | Sets the inter-byte spaces for all data byte fields. |
| linSetNAD | Changes the node address of the calling simulated slave. |
| linSetOEMDataInd | Sets/resets the data indication bit for a calling slave node. |
| linSetOEMDataIndTime | Sets the time in milliseconds after which a simulated slave automatically sets its data indication bit. |
| linSetOEMSleepInd | Sets/resets the sleep indication bit for a calling slave node. |
| linSetOEMWakeupInd | Sets/resets the wake-up indication bit for a calling slave node. |
| linSetRespBaudrate | Sets a response baud rate for a specified frame. |
| linSetRespCounter | Limits the number of responses sent for the specified frame identifier. |
| linSetRespError | Sets/resets the response error flag for a calling slave node. |
| linSetRespLength | Configures how many data bytes of the frame response should be sent. |
| linSetValidBreakLimits | Sets limits for the accepted sync break and delimiter lengths. |
| linUpdateResponse | Updates the response data of a specific LIN frame. |
| output | Applies frame header on the bus or reconfigures response data of LIN frame. |
| setSignal | Sets the transmitted signal to the accompanying value. |

| Functions | Short Description |
|---|---|
| linActivateGlobalNetworkManagement | Activates/deactivates network management for the entire LIN network. |
| linActivateSlaveNetworkManagement | Activates/deactivates network management for the calling Slave node. |
| linBusIsAwake | Inverts a specified bit when the next bus event for a specified ID occurs. |
| linCheckOEMDataInd | Checks the data indication bits of all slave nodes defined in the LIN network. |
| linCheckOEMSleepInd | Checks the sleep indication bits of all slave nodes defined in the LIN network. |
| linCheckOEMWakeupInd | Checks the wake-up indication bits of all slave nodes defined in the LIN network. |
| linCheckRespError | Queries the response_error flags of all Slave nodes defined in the LIN network. |
| linGetOEMDataInd | Queries the data indication bit of a Slave node. |
| linGetOEMSleepInd | Queries the sleep indication bit of a Slave node. |
| linGetOEMWakeupInd | Queries the wake-up indication bit of a Slave node. |
| linGetRespError | Queries the response error flag of the calling Slave node or of the Slave node. |
| linGotoSleep | Leads to a transmission of a go-to-sleep-command. |
| linGotoSleepInternal | Sets the LIN hardware to Sleep mode without sending a go-to-sleep-command on the network. |
| linSetOEMDataInd | Sets/resets the data indication bit for a calling slave node. |
| linSetOEMDataIndTime | Sets the time in milliseconds after which a simulated slave automatically sets its data indication bit. |
| linSetOEMSleepInd | Sets/resets the sleep indication bit for a calling slave node. |
| linSetOEMWakeupInd | Sets/resets the wake-up indication bit for a calling slave node. |
| linSetRespError | Sets/resets the response error flag for a calling slave node. |
| linSetWakeupBehavior | Defines the behavior after wake-up signal or an internal wake-up. |
| linSetwakeupCondition | Determines the conditions under which the LIN hardware can be reactivated (leaves the sleep mode). |
| linSetWakeupTimings | Configures wake-up timings. Wake-up timings can be configured per node for nodes defined in a LIN database. |
| linWakeupInternal | Wakes up the LIN bus without sending any wakeup signals. |
| linWakeup | Sends wakeup signals. |

| Message Events | Short Description |
|---|---|
| on linFrame | Is called on the receipt of a valid LIN frame. |
| Controller Events | Short Description |
| on linBaudrateEvent | Is called when the LIN hardware has successfully measured the baud rate of an external master or if the baud rate deviates by more than 0.5% from the last reported value. |
| on linDlcInfo | Is called when the LIN hardware has successfully measured the length of an unknown frame. |
| on linLongDominantSignal | Is called when the LIN hardware detects a long dominant signal on the bus. |
| on linSchedulerModeChance | Is called when modeled LIN Master switches from the current schedule table to another one. |
| on linSleepModeEvent | Is called when the wake status of the LIN hardware changes. |
| on linSpikeEvent | Is called when the LIN hardware detects a spike on the bus. |
| on linWakeupFrame | Is called when the LIN hardware detects a wake-up signal on the bus. |
| Error Events | Short Description |
| on linCsError | Is called when a frame was transmitted without a failure, but with an incorrect checksum. |
| on linReceiveError | Is called when an error occurred during a frame transmission. |
| on linSlaveTimeout | Is called for SlaveTimeouts. |
| on linSyncError | Is called when the LIN hardware was unable to become synchronized to an external master. |
| on linTransmError | Is called when no Slave responded to a transmission request. |

| Functions | Short Description |
|---|---|
| getSignal | Gets the value of a signal. |
| linBits2Time_ns | Converts specified bit time to an absolute time. |
| linBusIsAwake | Queries the awake state of the LIN bus. |
| linGetChecksum | Returns the checksum of a LIN frame or LIN checksum error. |
| linGetDlc | Queries the Data Length Code of a LIN frame. |
| linGetHWReceiveAccuracy | Queries the receive resolution of the LIN hardware. |
| linGetHWTransmitAccuracy | Queries the transmit resolution of the LIN hardware. |
| linGetMeasBaudrate | Retrieves results of a last baud rate measurement. |
| linGetMeasByteBitRates | This function calculates the bit rates for every byte which has been selected for edge time measurement. |
| linGetMeasEdgeTimeDiffs | Retrieves the time differences between edges. |
| linGetProtectedID | Calculates protected ID for the corresponding LIN frame identifier. |
| linGetResponseData | Queries LIN frame response data for specified FrameId on certain LIN channel. |
| linMeasEdgeTimeDiffs | Activates the measurement of the falling edges of the specified bytes in the next message. |
| linMeasHeaderBaudrate | Sets request to measure the baud rate value for next LIN header event. |
| linMeasRespBaudrate | Sets request to measure the baud rate value according to a certain data byte of a certain LIN frame. |
| linResetMaxHeaderLength | Resets the maximum header length to the protocol version dependent default. |
| linResetStatistics | Resets LIN channel statistics. |
| linSetBaudrateDetectionRange | Increases/decreases the baud rate detection range. |
| linSetMaxHeaderLength | Sets the maximum header length in bit times. |
| linSetRespTolerance | Sets the response tolerance for a specified frame in percent. |
| linSetValidBreakLimits | Sets limits for the accepted sync break and delimiter lengths. |
| linTime2Bits_ns | Converts specified system time to bit time. |

| Functions | Short Description |
|---|---|
| linDeactivateBitInversion | Cancels a previously activated bits inversion for LIN header or response. |
| linDetectMultipleErrors | Instructs LIN Hardware to enable/disable detection of more than one error per a LIN frame. |
| linDisturbHeaderWithBitStream | Configures the LIN hardware to disturb the next header with a bit stream. |
| linDisturbHeaderWithHeader | Configures the LIN hardware to disturb the next header with a new header. |
| linDisturbHeaderWithVariableBitStream | Configures the LIN hardware to disturb the next header with a variable bit stream. |
| linDisturbRespWithBitStream | Configures the LIN hardware to disturb the specified response with a bit stream. |
| linDisturbRespWithHeader | Configures the LIN hardware to disturb the specified response with a new header. |
| linDisturbRespWithVariableBitStream | Configures the LIN hardware to disturb the specified response with a variable bit stream. |
| linGetDominantTimeout | Returns the dominant timeout of the current channel’s transceiver in nanoseconds. |
| linInvertHeaderBit | Inverts the specified bit in the next LIN header. |
| linInvertHeaderBitEx | Inverts the specified number of 1/16th bits at the specified position in the next LIN header. |
| linInvertMultipleHeaderBits | Inverts the multiple bits in specified locations in the next LIN header. |
| linInvertMultipleRespBits | Inverts the multiple bits in specified locations in the next LIN header. |
| linInvertRespBit | Inverts the specified bit when the next bus event for the specified ID occurs. |
| linInvertRespBitEx | Inverts the specified number of 1/16th bits at the specified position in the next LIN frame’s response with the specified frame ID. |
| linResetRespDisturbance | Deactivates the disturbance in the response space of the specified frame. |
| linSendDominantSignal | Sends a dominant signal of a specified length. |
| linSetGlobalTimeoutPrevention | Activates/deactivates the global timeout prevention for transceivers with a dominant timeout. |
| linSetRespDisturbance | Activates a disturbance in the response space of the specified LIN frame. |
| linStartDisturbance | Starts a disturbance on the bus. |
| linStopDisturbance | Stops the disturbance on the bus. |

| Functions | Short Description |
|---|---|
| linActivateFlashMode | Activates the flash mode on high-speed capable transceivers. |
| linGetFallingEdgesOfDisturbedByte | Retrieves time stamps of all falling edges in the disturbed byte or in the pseudo-byte caused by the last bit inversion. |
| linIsBitStreamBusy | Queries the current LIN bit stream sending status. |
| linIsFlashModeActive | Reports the flash mode state on high-speed capable transceivers. |
| linResetManualChecksum | Sets the correct checksum of a LIN frame. |
| linResetRespBaudrate | Resets a response baud rate for a specified frame to the master baud rate. |
| linResetRespBitStream | Deactivates the bit stream response of the specified frame. |
| linSendBitStream | Sends an arbitrary bit stream on the LIN bus. |
| linSendHeaderError | Sends a header with the current sync break, sync delimiter and interbyte space settings and the specified sync byte and id byte. |
| linSendSamplingTestHeader | Sends a slave response header. |
| linSendVariableBitStream | Sends an arbitrary bit stream with bits of variable length. |
| linSetBaudrate | Changes the baud rate during the measurement. |
| linSetBreakLength | Changes length of break/synch symbol parts. |
| linSetChecksumError | Sets/resets a checksum error of a LIN frame. |
| linSetGlobalInterByteSpace | Changes the inter-byte space for all frame responses. |
| linSetInterByteSpace | Sets an inter-byte space for a specified frame and a specified byte filed. |
| linSetInterByteSpaces | Sets the inter-byte spaces for all data byte fields of all published frames of the calling LIN Slave node. |
| linSetInterframeSpace | Sets the minimum inter-frame space. |
| linSetManualChecksum | Sets a checksum (that is usually not a correct one) for a LIN frame. |
| linSetRespBaudrate | Sets a response baud rate for a specified frame. |
| linSetRespBitStream | Sets up a bit stream as the response to the specified frame. |
| linSetRespCounter | Limits the number of responses sent for the specified frame identifier. |
| linSetRespLength | Configures how many data bytes of the frame response should be sent. |
| linSetSchedulerJitter | Sets/resets the jitter mode and the jitter of the LIN hardware scheduler. |

| Note To use the CAPL functions the transport layer LINtp.DLL must be included.You can include the transport layer by using the configuration dialog of the node on page Components . The DLL is located in the Exec32 directory of your installation. The callback functions must be implemented in CAPL (see reference implementation for LINtp in Application Note: CANoe/CANalyzer as a Diagnostic Tool, chapter 4.5). |
|---|

| Functions | Short Description |
|---|---|
| Functions for Data Transfer |  |
| LINtp_ActivateFCTransmission | Activate the usage of FlowControl frames. |
| LINtp_DataReq | Send the given data. |
| LINtp_GetRxData | Retrieve data bytes received. |
| LINtp_InitAsMaster | Initializes the transport protocol in master role. |
| LINtp_SetFillByteValue | Sets fill byte used to pad frames. |
| LINtp_SetMaximumReceiveLength | Sets maximum number of bytes node can receive. |
| LINtp_SetNAD | Set node diagnostic address. |
| LINtp_SetSTmin | Sets the minimum separation time. |
| LINtp_SetWaiting | Sets ISO TP waiting state for the node. |
| Callback Functions |  |
| LINtp_DataCon | Receives the number of data bytes successfully sent. |
| LINtp_DataInd | Indicates the reception of data. |
| LINtp_FCPreTransmit | Each FlowControl frame is forwarded to this callback function before it is sent. |
| LINtp_FirstFrameIndication | Indicates the start of a segmented reception. |
| LINtp_PreSend | Each frame, sent by the transport layer, is forwarded to this callback before it is transmitted. |

| Selectors | Short Description |
|---|---|
| linBaudrateEvent | Detailed description of the linBaudrateEvent selectors. |
| linCsError | Detailed description of the linCsError selectors. |
| linDlcInfo | Detailed description of the linDlcInfo selectors. |
| linFrame | Detailed description of the linFrame selectors. |
| linHeader | Detailed description of the linHeader selectors. |
| linLongDominantSignal | Detailed description of the linLongDominantSignal selectors. |
| linReceiveError | Detailed description of the linReceiveError selectors. |
| linSchedulerModeChange | Detailed description of the linSchedulerModeChange selectors. |
| linSleepModeEvent | Detailed description of the linSleepModeEvent selectors. |
| linSpikeEvent Selectors | Detailed description of the linSpikeEvent selectors. |
| linSyncError | Detailed description of the linSyncError selectors. |
| linTransmError | Detailed description of the linTransmError selectors. |
| linWakeupFrame | Detailed description of the linWakeupFrame selectors. |

| Functions | Short Description |
|---|---|
| TestGetWaitEventMsgData | Calls up the frame content if a LIN frame with a valid response is the last event that triggers a wait instruction. |
| TestGetWaitLinCSErrorData | Retrieves the data of a checksum error triggered by the last wait instruction. |
| TestGetWaitLinETFSingleResponseData | Calls up the event content, if LIN Event-triggered frame with a single response for the specified associated frame is the last event that triggers a wait instruction. |
| TestGetWaitLinHdrData | Calls up the header content if LIN Header event is the last event that triggers a wait instruction. |
| TestGetWaitLinReceiveErrData | Calls up the error content if LIN Receive Error event is the last event that triggers a wait instruction. |
| TestGetWaitLinSyncErrorData | Retrieves the data of a synchronisation error that triggered the last wait instruction. |
| TestGetWaitLinTransmErrData | Calls up the error content if LIN Transmission Error event is the last event that triggers a wait instruction. |
| TestGetWaitLinWakeupData | Calls up the frame content if LIN Wakeup frame is the last event that triggers a wait instruction. |
| TestJoinLinCSErrorEvent | Adds an event of type checksum error to the set of joined events. |
| TestJoinLinETFSingleResponseEvent | Adds an event of type LIN event-triggered Frame with a single response for the specified associated frame to the set of joined events. |
| TestJoinLinHeaderEvent | Adds an event of type LIN Header to the set of joined events. |
| TestJoinLinReceiveErrorEvent | Adds an event of type LIN Receive Error to the set of joined events. |
| TestJoinLinSyncErrorEvent | Adds an event of type synchronisation error to the set of joined events. |
| TestJoinLinTransmErrorEvent | Adds an event of type LIN Transmission Error to the set of joined events. |
| TestJoinLinWakeupEvent | Adds an event of type LIN Wakeup frame to the set of joined events. |
| TestJoinMessageEvent | Adds an event of type LIN Unconditional/Event-triggered Frame to the set of joined events. |
| TestWaitForLinBitStreamStatus | Waits until the sending of a LIN bit stream is started or stopped. |
| TestWaitForLinCSError | Waits for a checksum error for the specified amount of time. |
| TestWaitForLinETFSingleResponse | Waits for the occurrence of a LIN Event-triggered frame with a single response for the specified associated frame. |
| TestWaitForLinHeader | Waits for the Header occurrence of the specified LIN frame. |
| TestWaitForLinReceiveError | Waits for the occurrence of LIN Receive Error event. |
| TestWaitForLinScheduleChange | Waits until the LIN scheduler reaches the specified table and slot index. |
| TestWaitForLinSyncError | Waits for a synchronisation error for the specified amount of time. |
| TestWaitForLinTransmError | Waits for the occurrence of LIN Transmission Error event. |
| TestWaitForLinWakeupFrame | Waits for the occurrence of LIN Wakeup frame. |
| TestWaitForMessage | Waits for the occurrence of LIN frame with a valid response. |

| Functions | Short Description |
|---|---|
| General Functions |  |
| ChkStart_AllNodesDead | This check reports a problem, if the node has not send any of its Tx messages within a given time-interval. |
| ChkStart_NodeDead |  |
| ChkStart_MsgDistViolation | This check is useful for spontaneous messages where one message depends to another message; e.g. for token-ring initializations for network management. |
| ChkStart_MsgSignalValueRangeViolation | This check is useful to supervise the value of signals. |
| ChkStart_MsgSignalValueInvalid |  |
| ChkStart_SignalCycleTimeViolation | Checks the occurrences of a signal. |
| ChkStart_SignalValueChange | Checks the physical value of a signal or an environment variable. |
| Functions to Observe a LIN Slave |  |
| ChkStart_LINDiagDelayTimesViolation | Checks the values of P2_min and ST_min. |
| ChkStart_LINETFViolation | Checks the format LIN Event-triggered frame response. |
| ChkStart_LINRespErrorSignal | Checks the LIN Response_Error signal. |
| ChkStart_LINRespToleranceViolation | Checks the LIN response transmission time. |
| Functions to Observe a LIN Master |  |
| ChkStart_LINHeaderToleranceViolation | Checks the LIN header transmission time. |
| ChkStart_LINMasterBaudrateViolation | Checks the LIN Master baud rate. |
| ChkStart_LINMasterInitTimeViolation | Checks an initialization time of LIN Master. |
| ChkStart_LINReconfRequestFormatViolation | Checks the format of LIN configuration requests. |
| ChkStart_LINSchedTableViolation | Checks a certain LIN schedule table for correspondence with the database definition. |
| ChkStart_LINSyncBreakTimingViolation | Checks the timing of the synchronization break field in LIN headers. |
| ChkStart_LINSyncDelTimingViolation | Checks the timing of the synchronization break field in LIN headers. |
| Functions to Observe LIN Network Management |  |
| ChkStart_LINWakeupReqLengthViolation | Checks the length of LIN wake-up request. |
| ChkStart_LINWakeupRetryViolation | Checks number of LIN wake-up signals and the time between them. |

| Version 15© Vector Informatik GmbH |
|---|
