# diagGetCommParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetCommParameter (char paramName[]); // form 1
long diagGetCommParameter( char paramName[], dword index, char buffer[], dword bufferLen); // form 2
long DiagGetCommParameter(char ecuQualifier[], long isTester, char paramName[]); // form 3
long DiagGetCommParameter(char ecuQualifier[], long isTester, char paramName[], dword index, char buffer[], dword bufferLen); // form 4
```

## Description

Returns the value of a numeric/textual communication parameter of the given or currently active diagnostic description. The values are read from the diagnostic description if they cannot be set in the configuration dialog.

## Parameters

| Name | Type | Description |
|---|---|---|
| Qualifier | Available in | Description |
| CANoe.AddressMode |  | ISO TP address mode: 0: Normal 1: Extended 2: NormalFixed 3: Mixed <0: No ISO TP |
| CANoe.TxId | [0 1*] | CAN Id for transmitted frames |
| CANoe.RxId | [0 1*] | CAN Id for received frames |
| CANoe.BaseAddress | [1*] | TP base address |
| CANoe.EcuAddr | [1 2 3] | Number of this node |
| CANoe.TgtAddr | [1 2 3] | Target node number |
| CANoe.AddrExt | [3] | Address extension byte |
| CANoe.TxPrio | [2 3] | Frame transmit priority |
| Note 1*: Extended address can be operated on two different types: With base address With free assignment of the TX- and RX-Id The parameter values are each determined from the viewing angle of the corresponding node. Therefore, in an ECU simulation with normal addressing, the TX-Id represents the RX-Id, which is included in the tester node. |  |  |
| Qualifier |  | Description |
| CANoe.UudtId |  | If the ECU delivers responses also via UUDT frames, their CAN-Id can be determined here as well. |
| CANoe.Blocksize |  | ISO TP parameter, number of consecutive frames between two flow control frames. |
| CANoe.STmin |  | ISO TP parameter, minimum interval [ms] between sent consecutive frames, which the sender should maintain. |
| CANoe.FCDelay |  | ISO TP parameter, delay of flow control frames sent. |
| Timing Parameter with ISO 15765-3: |  |  |
| CANoe.S3ClientTime |  | Time the diagnostic client (=tester) should wait before sending a tester present request.This value is also returned for the deprecated qualifier CANoe.S3Time. |
| CANoe.S3ServerTime |  | Timeout in the diagnostic server for leaving a non-default session. |
| CANoe.P3TimePhys |  | Minimum waiting time after physical transmitting of a request. |
| CANoe.P3TimeFunc |  | Minimum waiting time after functional transmitting of a request. |
| Values |  |  |
| -1 |  | No padding (i.e. DLC variable) |
| 0..255 |  | Use this value to pad to DLC=8. |
| <-1 |  | Normal diagnostic error codes. |
| rest |  | reserved |
| Values |  |  |
| 0 |  | Use the values of the first flow control frame only. |
| 1 |  | Use the values from ALL flow control frames. |
| Values |  |  |
| 0 |  | Use the TX priority given. |
| 1 |  | Use the priority of the received "first frame" as priority of flow control frame. |
| CANoe.FirstSN |  | 0..15: The sequence number sent in the first "consecutive frame". |
| CANoe.BSOff |  | 0..255: Block size value indicating "do not expect further flow controls". |
| CANoe.FixedFrameLength |  | 0..8: All CAN frames should have at least this many bytes. |
| CANoe.MaxMessageLength |  | Maximum accepted length of a ISO TP message. |
| DoIP.VEHICLE_Adapter (replaces DoIP.VEHICLE_Interface) | See DoIP_SetVehicleAdapter (replaces DoIP_SetVehicleInterface) | form 2 |
| DoIP.TESTER_Adapter | See DoIP_SetTesterAdapter | form 2 |
| DoIP.VEHICLE_Address | See DoIP_SetVehicleAddress | form 2 |
| DoIP.VEHICLE_LogicalAddress | Returns the logical DoIP address of the DoIP entity. | form 1 |
| DoIP.VEHICLE_UDP_Data | See DoIP_SetVehicleUdpPort | form 1 |
| DoIP.VEHICLE_TCP_Data | See DoIP_SetVehicleTcpPort | form 1 |
| DoIP.TESTER_LogicalAddress | Returns the logical DoIP address of the test equipment. | form 1 |
| DoIP.TESTER_UDP_Data | See DoIP_SetTesterUdpPort | form 1 |
| DoIP.T_TCP_Generic_Inactivity | See DoIP_SetGenericTimeout | form 1 |
| DoIP.T_TCP_Initial_Inactivity | See DoIP_SetInitialTimeout | form 1 |
| DoIP.T_TCP_Alive_Check | See DoIP_SetAliveCheckTimeout | form 1 |
| DoIP.VehicleSimulationVIN | Returns the VIN from Vehicle Simulation Parameter area as text in parameter buffer. | form 2 |
| DoIP.VehicleSimulationEID | Returns the EID from Vehicle Simulation Parameter area as text in parameter buffer. | form 2 |
| DoIP.VehicleSimulationGID | Returns the GID from Vehicle Simulation Parameter area as text in parameter buffer. | form 2 |
| DoIP.Protocol | Configured DoIP protocol, see DoIP_SetProtocol. | form 1 |
| DoIP.TESTER_PreferIPv6 DoIP.VEHICLE_PreferIPv6 | Returns 6 if the IPv6 address of the local adapter shall be preferred. See DoIP_SetLocalIPaddressVersion. | form 1 |
| DoIP.ActivationLineStartuptime | Returns the time configured for that the activation line shall be active at measurement start before the vehicle can be accessed. See Activation Line (DoIP). | form 1 |
| DoIP.GatewayAddress | Returns the logical address of the gateway entity that is used to reach the target. See DoIP_SetGatewayLogicalAddress. | form 1 |
| DoIP.FunctionalAddress | Returns the logical address used for functional communication. Use DoIP_AddECU in a vehicle simulation to allow reception of such requests, and DoIP_SetVehicleLogicalAddress in a tester to send a request functionally. | form 1 |
| DoIP.ReconnectDelay | See DoIP_Set/GetReconnectDelay | form 1 |
| DoIP.ReconnectInterval | See DoIP_GetReconnectInterval and DoIP_SetReconnectInterval. | form 1 |
| DoIP.ReconnectMaxAttempts | See DoIP_GetReconnectInterval and DoIP_SetReconnectInterval. | form 1 |
| DoIP.ActivationLineSysvar DoIP.ActivationLineSysvar-Namespace | Return the system variable configured for the DoIP activation line. See Activation Line (DoIP) for details. | form 2 |
| DoIP.TESTER_IPAddress | Returns IP address the tester shall use for sending. Use DoIP_SetLocalIPaddress in a tester node. | form 2 |
| DoIP.VEHICLE_IPAddress | Returns the IP address the vehicle simulation shall listen on. Use DoIP_SetLocalIPaddress in a vehicle Simulation. | form 2 |
| Note For details and an example please refer to the reference implementation of the K-Line CAPL Callback Interface for diagnostics that is installed under <application>\Reusable\CAPL_Includes\Diagnostics\CCI_KLine.cin and can be included in CAPL programs with #include "Diagnostics\CCI_KLine.cin" |  |  |
| KLine.5BaudAddress |  | Address sent in the 5 baud wakeup pattern.See KLine_Set5BaudAddressTester |
| KLine.Baudrate |  | Configured baud rate |
| KLine.DataBits |  | Number of data bits configured |
| KLine.EcuAddress |  | Address of the ECU |
| KLine.ForceLengthByte |  | Shall an address byte be sent always?See KLine_SetHeaderFormat |
| KLine.FunctionalAddress |  | Address of the functional group |
| KLine.InitType |  | Initialization mode used.See KLine_SetInitType> |
| KLine.P3min |  | K-Line timing parameter P3.See KLine_SetP3Tester |
| KLine.P4min |  | K-Line timing parameter P4.See KLine_SetP4Tester |
| KLine.Parity |  | UART configuration parameter.See KLine_SetUARTParameter |
| KLine.StopBits |  | UART configuration parameter.See KLine_SetUARTParameter |
| KLine.TIdle |  | K-Line idle time. |
| KLine.TIniL |  | Fast initialization parameter.See KLine_SetWakeUpTimesTester and _KLine_FastInitPatternReceived |
| KLine.TWup |  | Fast initialization parameterSee KLine_SetWakeUpTimesTester and _KLine_FastInitPatternReceived |
| KLine.TesterAddress |  | Address the tester shall use. |
| KLine.UartConfig |  | Encoded UART parameters, see KLine.DataBits, KLine.Parity and KLine.StopBits |
| KLine.W1max |  | K-Line timing parameter W1 (max) for 5 baud init pattern |
| KLine.W2max |  | K-Line timing parameter W2 (max) for 5 baud init pattern |
| KLine.W3max |  | K-Line timing parameter W3 (max) for 5 baud init pattern |
| KLine.W4max |  | K-Line timing parameter W4 (max) for 5 baud init pattern KLine_SetW4Tester |
| KLine.W4min |  | K-Line timing parameter W4 (min) for 5 baud init pattern KLine_SetW4Tester |
| index |  | Set to 0. |
| buffer |  | Buffer to retrieve string parameters. |
| bufferLen |  | Size of the buffer in bytes. |
| ecuQualifier |  | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |
| isTester |  | 0: The node asking for the communication parameter is an ECU simulation 1: The node asking for the communication parameter is a tester other: reserved |

## Return Values

Error code or value of the parameter.

## Example

You can find examples for this function in the CAPL callback interface (CCI) reference implementations.See Diagnostics: Connection of the Communication Layer for details.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1: form 1, 2 9.0 SP3; form 3, 4 | — | — | — | 1.0: form 1, 2 2.1 SP3: form 3, 4 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
