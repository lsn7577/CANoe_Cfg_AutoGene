# linTime2Bits

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by linTime2Bits_ns. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword linTime2Bits(dword time) |  |  |  |
| linTime2Bits(dword channel, dword time) |  |  |  |  |
| Function | This function converts specified system times to bit times. The conversion is done using the current baud rate on the channel determined by the CAPL program context. Note Calling this function with the explicit channel is only possible from a CAPL program defined in the Measurement Setup of CANoe. | Note Calling this function with the explicit channel is only possible from a CAPL program defined in the Measurement Setup of CANoe. |  |  |
| Note Calling this function with the explicit channel is only possible from a CAPL program defined in the Measurement Setup of CANoe. |  |  |  |  |
| Parameters | time System time to be converted [in units of 10 µsec]. |  |  |  |
| channel Channel number, whose baud rate will be used. |  |  |  |  |
| Return Values | Resulting bit time. |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | LIN | — | • |  |
| 6.0 | LIN | • | • |  |
| Example Extract sync break length of LIN frames on linFrame *{dword sysTimeSyncBreak; // time in 10µs unitsdword bitTimeSyncBreak; // time in bit time unitssysTimeSyncBreak = linGetSyncBreakLength(this);bitTimeSyncBreak = linTime2Bits(sysTimeSyncBreak);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
