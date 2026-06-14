# Return Values (Diagnostics)

> Category: `Diagnostics` | Type: `notes`

## Description

TFS functionality is only available in test modules, e.g. waiting for a response with testWaitForDiagResponse or writing a diagnostic object to the test report with testReportWriteDiagObject.

The Seed & Key DLL does not contain a suitable Seed & Key function.

Configure a Seed & Key DLL that holds the expected Seed & Key function.

See Basics of Diagnostic Session Control and Seed & Key DLL / Security Access for details.

| Return Value | Error Notification | Description | ToDo |
|---|---|---|---|
| 0 | No error, success. |  |  |
| >0 | Number, e.g. length of the given text. |  |  |
| -100 | The input provided on function call is not consistent or sufficient. | The arguments provided to a CAPL function call are not usable. Examples are: exceeding a range for a parameter value or byte position. | Check the arguments provided to the function call. |
| -99 | The object's response is pending, therefore cannot delete it. | The diagnostic object is still in use, therefore the operation is not possible. | Delay the operation until the object is no longer accessed. |
| -98 | The handle is not assigned to a diagnostic object. Invalid diagnostic object handle encountered! No diagnostic description for ECU qualifier '...' found! | A diagnostic object was referred to that does not (no longer) exist, or there is no target with the given qualifier. | Check that the initialization of the object worked, i.e. diagSetTarget was successful. Make sure that the object is valid in the current target's context, i.e. the service it is declared with is defined in the target's description. When accessing the last response stored at a request, make sure that a response has been received for the request. |
| -97 | The parameter does not exist in this object, or is constant. Parameter '...' not found or has wrong type! Parameter '...' is declared constant! Error accessing complex parameter: '...', sub-parameter '...' not found or constant. | An operation on a parameter is not possible, because it cannot be found or is not accessible. | Make sure that the parameter exists in the diagnostic object. Some primitives may hold different parameters depending on their data. If a parameter is declared constant in the description, its value cannot be changed. If the type of a parameter does not allow the operation specified, this error will be given. |
| -96 | Function not implemented yet. | The function called has not been implemented yet. |  |
| -95 | Accessing CANdelaLib lead to error '...' for '...' Parameter or object '...' not defined! Value conversion for parameter '...' failed: ... | An operation performed on the diagnostic objects contradicts the definitions in the diagnostic descriptions. | The details in the warning will provide additional information. Make sure the parameter is defined in the accessed diagnostic object. Make sure to provide a valid symbolic/physical parameter value for conversion. |
| -94 | Diagnostics was not initialized for the node, i.e. no SetEcu/Target called. Diagnostics not initialized! A tester must call diagSetTarget() e.g. Network request interface not found! | The operation is not possible because diagSetTarget has not been called in a tester yet, or there is no diagnostic description assigned to the simulation node (for diagnostic server simulation). | Make sure diagSetTarget is called and sets an existing target successfully. A network description has to be selected in order to use certain network request functions. Assign a diagnostic description to the ECU simulation node. |
| -93 | The specified callback was not found. | Please refer to Diagnostics: Connection of the Communication Layer for details on the CAPL callback interface. |  |
| -92 | There was an error on TP level. | The transport protocol (TP) layer has reported a transmission error. | Check the Write window for further information. Check the communication sequence in the Trace window for possible problems. |
| -91 | Only one request/response can be sent at a time! | It is possible to send only one diagnostic object at a time, i.e. while the object is processed for sending, no other object can be sent. | Make sure that the processing of the previous object is finished. |
| -90 | Test function outside TestCase, or Tester-only function called in ECU, or vice-versa. | Some functionality is only available in a tester or a test case in a test module. | Requests can only be sent from nodes configured as tester, i.e. diagSetTarget must have been called successfully. Responses can only be sent from nodes configured to be diagnostic server simulations, i.e. a diagnostic description must have been assigned to them. TFS functionality is only available in test modules, e.g. waiting for a response with testWaitForDiagResponse or writing a diagnostic object to the test report with testReportWriteDiagObject. |
| -89 | No seed and key library was specified. | No Seed & Key DLL was specified in the diagnostic configuration. | Configure a Seed & Key DLL. |
| -88 | The Seed & Key library did not contain a matching Seed & Key function. | The Seed & Key DLL does not contain a suitable Seed & Key function. | Configure a Seed & Key DLL that holds the expected Seed & Key function. See Basics of Diagnostic Session Control and Seed & Key DLL / Security Access for details. |
| -87 | The seed and key library couldn't be loaded. | Ensure that the correct Seed & Key path and file name is configured. |  |
| -86 | The buffer was too small. | Increase the buffer size. |  |
| -85 | The seed array size is too large. | Decrease the seed array size. |  |
| -84 | The security level is invalid. | Use a correct security level. |  |
| -83 | The variant is invalid. | Use a supported variant. |  |
| -82 | An unspecified error occurred. |  |  |
| -81 | The function cannot perform the action because of wrong HW, e.g. K-Line interface required instead of a serial port. | Ensure correct HW devices. |  |
| -80 | No matching request was found to perform the action. | This happens e.g. during testReportWriteEcuInformation when no request with constant parameters was found. |  |
| -79 | No diagnostic channel found. | The diagnostic channel could not be opened. |  |
| -78 | No suitable class or request was found. | Ensure that the qualifiers are defined in the diagnostic description. |  |
| -77 | A time out happened. | The ECU did not send a response for the request. |  |
| -76 | Transmission failed. | The request or response could not be sent. |  |
| -75 | The class was not found in the diagnostic description. | Ensure that the class qualifiers is defined in the diagnostic description. |  |
| -74 | Creation of the PDU bytes for a diagnostic object failed! Parameters without defaults may have to be set, e.g. | It was not possible to create a byte sequence for a diagnostic CAPL object, therefore the CAPL function called cannot work. For example, it is not possible to send the request on the network. | Make sure that all parameters in the object are set to valid values, especially mandatory parameters without defaults. Check the corresponding service definition in the diagnostic description. |
| -73 | During processing a negative response was received. | Ensure that the ECU responds correctly. |  |
| -72 | No key could be calculated. | Ensure that the correct Seed & Key DLL is configured. |  |
| -71 | The key was not accepted. | Ensure that the correct Seed & Key DLL is configured. |  |
| -70 | The diagnostic object is too small. | The specified element does not exist in the object. | Check the index used. |

| Note For the following return values please check the security source and the configuration of the security manager. |
|---|

| Return Value | Authentication or Authorization Result |
|---|---|
| -199 | Authentication rejected |
| -198 | Authentication tool is not properly configured, i.e. security manager not available or channel not ready |
| -197 | This mode is not implemented |
| -196 | Invalid handle |
| -195 | Error in security source |
| -194 | Security not usable |
| -193 | Data missing |
| -192 | Signal length mismatch |
| -191 | General error |

| Version 15© Vector Informatik GmbH |
|---|
