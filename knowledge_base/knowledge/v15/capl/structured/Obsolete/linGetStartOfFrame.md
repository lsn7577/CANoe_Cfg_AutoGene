# linGetStartOfFrame

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by linFrame selectors, linCsError selectors, linReceiveError selectors, linTransmError selectors, linSyncError selectors and linWakeupFrame selectors. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword linGetStartOfFrame(linFrame busEvent) |  |  |  |
| dword linGetStartOfFrame(linCSError busEvent) |  |  |  |  |
| dword linGetStartOfFrame(linReceiveError busEvent) |  |  |  |  |
| dword linGetStartOfFrame(linTransmError busEvent) |  |  |  |  |
| dword linGetStartOfFrame(linSyncError busEvent) |  |  |  |  |
| dword linGetStartOfFrame(linWakeupFrame busEvent) |  |  |  |  |
| Function | This function can be used to retrieve a start time stamp of a LIN bus event. The resulting time stamp is a time elapsed since the measurement start [in units of 10 µsec]. |  |  |  |
| Parameters | busEvent LIN bus event of type frame, checksum error, receive error, transmission error, synchronization error or wakeup signal. |  |  |  |
| Return Values | Returns the retrieved time stamp [in units of 10 µsec] or 0 on failure. |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | LIN | • | • |  |
| Example Calculate header length [in bit times] for each received LIN frame on linFrame *{dword startOfFrame, endOfHeader, headerLength;if (this.dir != RX){return; // ignore transmitted frames}startOfFrame = linGetStartOfFrame(this); // retrieve frame start time endOfHeader = linGetEndOfHeader(this); // retrieve header end timeheaderLength = linTime2Bits(endOfHeader - startOfFrame); // calculate header length in bit times// display the result in Write windowwriteLineEx(0,0, "Header length for LIN frame with identifier 0x%x is %d bit times", this.ID, headerLength);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
