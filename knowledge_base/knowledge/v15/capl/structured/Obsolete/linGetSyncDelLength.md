# linGetSyncDelLength

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by linFrame selectors, linCsError selectors, linReceiveError selectors, linTransmError selectors and linSyncError selectors. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword linGetSyncDelLength(linFrame busEvent) |  |  |  |
| dword linGetSyncDelLength(linCSError busEvent) |  |  |  |  |
| dword linGetSyncDelLength(linReceiveError busEvent) |  |  |  |  |
| dword linGetSyncDelLength(linTransmError busEvent) |  |  |  |  |
| dword linGetSyncDelLength(linSyncError busEvent) |  |  |  |  |
| Function | This function can be used to retrieve the synch delimiter (recessive bits) length of a LIN bus event. The resulting length is in units of 10 µsec (microseconds).To get the result in bit times linTime2Bits() function can be used. |  |  |  |
| Parameters | busEvent LIN bus event of type frame, checksum error, receive error, transmission error, synchronization error or wakeup signal. |  |  |  |
| Return Values | Returns the retrieved length [in units of 10 µsec] or 0 on failure. |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | LIN | • | • |  |
| Example Analyze receive error event by retrieving length of synch break and sync delimiter on linReceiveError{dword timelenBreak,timelenDel;dword bitlenBreak,bitlenDel;timelenBreak = linGetSyncBreakLength(this); // retrieve break length in time unitsbitlenBreak = linTime2Bits(timelenBreak); // convert time units to bit timestimelenDel = linGetSyncDelLength(this); // retrieve delimiter length in time unitsbitlenDel = linTime2Bits(timelenDel); // convert time units to bit times...} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
