# linSendSleepModFrm

> Category: `Obsolete` | Type: `notes`

## Description

Frame length is 2 bytes. The data bytes remain not changed.

Frame length is 8 bytes. The first data byte is set to 0, the other data bytes remain not changed.

| Deprecated Function Replaced by linGotoSleep and linGotoSleepInternal |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long linSendSleepModFrm (long silent, long restartScheduler, long wakeupIdentifier) |  |  |  |
| Function | This function leads to a transmission of a go-to-sleep-command. Frame identifier and data byte values of that command depend on the used LIN specification: 0: LIN specification 1.1 and older Frame length is 2 bytes. The data bytes remain not changed. 0x3C: LIN specification 1.2 and newer Frame length is 8 bytes. The first data byte is set to 0, the other data bytes remain not changed. Calling this function in the event procedure on preStart (parameter silent = 1) leads to measurement start in Sleep mode. |  |  |  |
| Parameters | silent When this flag is set the LIN hardware switches to Sleep mode without sending a go-to-sleep-command before. By this way the LIN hardware can be switched to Sleep mode even it is not the Master. So the BusIdle timeout is reduced. Value range: 0 .. 1 |  |  |  |
| restartScheduler Determines if index of the slot to be started with after wake-up has to be reset, i.e. it becomes 0. If it’s not reset the next slot before entering sleep mode is used In the case no schedule tables are defined this parameter is ignored. Value range: 0 .. 1 |  |  |  |  |
| wakeupIdentifier LIN frame identifier to be sent additionally directly after sending a wake-up signal. If an invalid identifier is specified i.e. not in the range 0 .. 63: when schedule tables are defined no special wake-up identifier is sent; when no schedule tables are defined a "SynchBreak / SynchField" pair without an identifier is sent; Value range: 0 .. 0xFF |  |  |  |  |
| Return Values | On success, a value unequal to zero, otherwise zero. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP4 | LIN | — | • |  |
| Example Start measurement in Sleep mode on preStart{linSendSleepModFrm(1, 0 , 0x1); // use 0x1 as wake-up identifier}or// send go-to-sleep-command during measurement...linSendSleepModFrm(0, 0 , 0xFF); // explicit sleep frame, no wake-up identifier |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
