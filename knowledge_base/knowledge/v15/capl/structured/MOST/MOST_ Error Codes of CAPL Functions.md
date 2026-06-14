# MOST: Error Codes of CAPL Functions

> Category: `MOST` | Type: `notes`

| Error Code | Description |
|---|---|
| kMostOK = 0 | No Error occurred. |
| kMostInvalidChannel = -1 | The operation was requested for an invalid channel number. |
| kMostNoConnection = -2 | The driver was unable to establish a connection to the MOST interface hardware.Check the connection settings in the Hardware Configuration dialog under the menu path Configuration\|Hardware Configuration. |
| kMostIllegalTime = -3 | The function was called in the wrong phase of the measurement. For example the OptoLyzer mode can only be changed in the ‘preStart’ function. |
| kMostWrongThread = -4 | For technical reasons this function may not be called from this area of CANoe.Not all functions can be called from CAPL nodes in the analyzing setup. |
| kMostWrongHWMode = -5 | The hardware interface to the MOST bus is in a state in which the called function is unavailable. |
| kMostTxQueueFull = -6 | The transmit queue of 256 Messages is full, while trying to send another message. |
| kMostHWBusy = -7 | Unable to perform the desired action due to hardware overload. |
| kMostWrongHWType = -8 | This functionality is not supported by the hardware used. |
| kMostParameterOutOfRange = -9 | One or more function parameters lie outside of their valid value ranges. |
| kMostDriverCallFailed = -10 | The MOST hardware driver returned an error. Please make sure that the driver has been properly installed and that the hardware is operationally ready. |
| kMostAsInvalidChannel = -21 | The function was called for an invalid channel. |
| kMostAsDoubleOp = -22 | The function cannot be executed, because its results already apply.(e.g. a CAPL node has already been registered in the Local FBlockList) |
| kMostAsIllegalTime = -23 | The function cannot be executed in this phase of the simulation cycle. |
| kMostAsParamNotAvailable = -24 | The requested parameter value is unavailable. |
| kMostAsNotAvailable = -25 | The function is unavailable or the MOST Application Socket is inactive. |
| kMostAsBeforeNetOn = -26 | This function can not be called before NetOn. |
| kMostAsInvalidParameter = -29 | At least one parameter passed with the function lies outside of its valid value range. |
| kMostXML4CAPLGeneralExecError = -30 | General execution error. |
| kMostXML4CAPLUnknownMsg = -31 | The specified message cannot be dissolved with the available function catalogs. |
| kMostXML4CAPLMsgSizeExceeded = -32 | The function cannot be executed, since the size of the specified message is exceeded. |
| kMostXML4CAPLUnknownParamAdr = -33 | The specified parameter address cannot be dissolved with the available function catalogs. |
| kMostXML4CAPLParamNotFoundInMsg = -34 | A parameter with the indicated address cannot be found in the message. |
| kMostXML4CAPLParamTypeMismatch = -35 | The function has attempted to read a value that does not have the compatible data type. |
| kMostXML4CAPLEncodingMismatch = -36 | The function cannot read the string or raw data, since the coding does not match. |

| Version 15© Vector Informatik GmbH |
|---|
