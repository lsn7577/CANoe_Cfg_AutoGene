# linGetEndOfHeader

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by linFrame selectors, linCsError selectors and linReceiveError selectors. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword linGetEndOfHeader(linFrame busEvent) |  |  |  |
| dword linGetEndOfHeader(linCSError busEvent) |  |  |  |  |
| dword linGetEndOfHeader(linReceiveError busEvent) |  |  |  |  |
| Function | This function can be used to retrieve a time stamp of the header part for a certain LIN bus event. The resulting time stamp is a time elapsed since measurement start [in units of 10 µsec]. Note The time returned by this function corresponds to the end of the Protected ID field as detected by an UART. For the XL-hardware, this includes 9/16 of the stop bit. To calculate the theoretical end of Protected ID field including the stop bit, 7/16 of a bit time should be added. Similarly to calculate the start of the Protected ID field, 9 and 9/16 bit times should be subtracted. | Note The time returned by this function corresponds to the end of the Protected ID field as detected by an UART. For the XL-hardware, this includes 9/16 of the stop bit. To calculate the theoretical end of Protected ID field including the stop bit, 7/16 of a bit time should be added. Similarly to calculate the start of the Protected ID field, 9 and 9/16 bit times should be subtracted. |  |  |
| Note The time returned by this function corresponds to the end of the Protected ID field as detected by an UART. For the XL-hardware, this includes 9/16 of the stop bit. To calculate the theoretical end of Protected ID field including the stop bit, 7/16 of a bit time should be added. Similarly to calculate the start of the Protected ID field, 9 and 9/16 bit times should be subtracted. |  |  |  |  |
| Parameters | busEvent LIN bus event of type frame, checksum error or receive error. |  |  |  |
| Return Values | Returns the retrieved time stamp [in units of 10 µsec] or 0 on failure. |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | LIN | • | • |  |
| Example Retrieve time stamps of header (ID byte) on analyzing a receive error event on linReceiveError{long byteIndex; dword endHeaderTime;endHeaderTime = linGetEndOfHeader(this);...} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
