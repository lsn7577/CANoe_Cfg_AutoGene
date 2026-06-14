# K-Line CAPL Functions

> Category: `KLine` | Type: `notes`

## Description

Callbacks

Configuring and Controlling a K-Line ECU Simulation

Configuring and Controlling a K-Line Tester

Controlling a Diagnostic Channel

Test Feature Set for K-Line

| K-LINE Only available with K-Line. |
|---|

| Callbacks Configuring and Controlling a K-Line ECU Simulation Configuring and Controlling a K-Line Tester | Controlling a Diagnostic Channel Test Feature Set for K-Line |
|---|---|

| Functions | Short Description |
|---|---|
| _Diag_ChannelStateChanged | Indicates the state of the diagnostic channel. |
| _Diag_PreSend | Is called before a frame is transmitted. |
| _KLine_ByteReceptionInd | Is called when a byte has been received. |
| _KLine_ByteTransmissionCon | Is called when a byte has been transmitted. |
| _KLine_DataCon | Called for a transmitted K-Line response. |
| _KLine_DataInd | Called for a received K-Line request. |
| _KLine_ErrorInd | Called when a protocol error occurred. |
| _KLine_FastInitPatternReceived | Called when a fast init pattern has been received. |
| _KLine_FrameReceptionInd | Is called when a frame has been received. |
| _KLine_FrameTransmissionCon | Is called when a frame has been transmitted. |

| Functions | Short Description |
|---|---|
| DiagInitEcuSimulation | Initialize CAPL node to represent a diagnostics ECU simulation. |
| DiagSendResponsePDU | Sends a raw byte buffer. |
| KLine_CreateECURepresentation | Initialize K-Line ECU communication on given channel. |
| KLine_Init5BaudEcuParams | Initialize K-Line channel for reception of the 5 baud pattern. |
| KLine_ResetECUConnection | Resets the connection state of the simulated ECU. |
| KLine_SendFrame | Send data on the active K-Line communication channel. |
| KLine_SetP1ECU | Sets the interbyte time of a response. |
| KLine_SetP2max | Sets the maximum time between the client request and the server response, or between 2 server responses. |
| KLine_SetP3max | Sets the maximum time between the end of the server response and start of a new client request. |

| Functions | Short Description |
|---|---|
| DiagSendRequestPDU | Sends a raw byte buffer. |
| KLine_EnableSegmentedResponses | Enables receiving segmented responses. |
| KLine_GetMeasuredInitParameter | Retrieves the different parameters of the init patterns. |
| KLine_Set5BaudAddressTester | Sets the 5 baud address for the 5 baud init pattern. |
| KLine_SetBaudrate | Allows changing the baud rate during the measurement. |
| KLine_SetECUAddress | Sets the address of the ECU. |
| KLine_SetFunctionalAddress | Sets the functional address of the ECU. |
| KLine_SetHeaderFormat | Configures the used header format. |
| KLine_SetInitType | Configures the used initialization pattern. |
| KLine_SetP3Tester | Sets the P3 time which the tester waits until transmitting a further request. |
| KLine_SetP4Tester | Sets the interbyte time of a request. |
| KLine_SetTesterAddress | Sets the address of the tester. |
| KLine_SetUARTParameter | Configures the way bytes are sent on K-Line. |
| KLine_SetW4Tester | Sets the W4 timing of the tester between keybyte2 and keybyte2Not. |
| KLine_SetW5Tester | Sets the W5 timing befor the tester starts to transmit the address byte. |
| KLine_SetWakeUpTimesTester | Sets the timings of the fast init wake-up pattern. |
| KLine_SuppressAutomaticStopCommunication | For a fast init ECU, automatic sending of a Stop communication command will be suppressed after closing the channel or a S3 timeout. |
| KLine_UseDefaultHeader | The header format specified in the diagnostic description file will be used. |

| Functions | Short Description |
|---|---|
| DiagCloseChannel | Closes a channel. |
| DiagConnectChannel | Connects a channel. |
| DiagDisconnectChannel | Disconnects a channel. |
| DiagIsChannelConnected | Checks if a channel is already in state Connected. |

| Functions | Short Description |
|---|---|
| TestGetWaitEventKLineByte | If a byte is the last event that triggers a wait instruction, the content can be called up with this function. |
| TestGetWaitEventKLineFrame | If a K-Line frame is the last event that triggers a wait instruction, the content can be called up with this function. |
| TestWaitForDiagChannelClosed | Waits for the occurrence of the state change of a diagnostic channel to the state Closed. |
| TestWaitForDiagChannelConnected | Waits for the occurrence of the state change of a diagnostic channel to the state Connected. |
| TestWaitForDiagKLineByteReceived | Waits for the occurrence of a received byte. |
| TestWaitForDiagKLineByteTransmitted | Waits for the occurrence of a transmitted byte. |
| TestWaitForDiagKLineFrameReceived | Waits for the occurrence of a received valid message. |
| TestWaitForDiagKLineFrameTransmitted | Waits for the occurrence of a transmitted valid message. |

| Version 15© Vector Informatik GmbH |
|---|
