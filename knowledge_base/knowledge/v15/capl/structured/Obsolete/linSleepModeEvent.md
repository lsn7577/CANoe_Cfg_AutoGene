# linSleepModeEvent

> Category: `Obsolete` | Type: `notes`

## Description

—

| Deprecated Function Replaced by the event procedure on linSleepModeEvent. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Function Syntax | void linSleepModeEvent(long syncTimeStamp, long origTimeStamp, int wasAwake, int isAwake, int externalCause, int reason) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function | Is called whenever a SleepModeEvent (not SleepModeFrame) is received. The time stamps are the same as by LINRcvFrame. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Parameters | wasAwake If this flag is set, the LIN hardware was active before the Event occurred.If not, the LIN hardware was in Sleep mode before the Event occurred. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| isAwake If this flag is set, the LIN hardware's present state is active.If not, the LIN hardware's present state is Sleep mode. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| externalCause If this flag is set, the Event is caused by an external event (e.g. SleepModeFrame, WakeupFrame or bus traffic).If not, the Event is caused by an internal event (e.g. SleepModeFrame, WakeupFrame, SilentSleepMode command or BusIdle timeout). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| reason This value returns the cause of the Event. One of the following values can be returned. General values: 0 Start state Values while switching to Sleep mode: 1 SleepModeFrame 2 BusIdle timeout 3 "silent SleepMode" command (to reduce the BusIdle timeout) Values while leaving the Sleep mode: 9 External Wakeup signal 10 Internal Wakeup signal 11 Bus traffic (only occurs while the LIN hardware is not the Master) Values, if the LIN hardware does not switch to Sleep mode in spite of a request: 18 Bus traffic (only occurs while the LIN hardware is not the Master) | 0 | Start state | 1 | SleepModeFrame | 2 | BusIdle timeout | 3 | "silent SleepMode" command (to reduce the BusIdle timeout) | 9 | External Wakeup signal | 10 | Internal Wakeup signal | 11 | Bus traffic (only occurs while the LIN hardware is not the Master) | 18 | Bus traffic (only occurs while the LIN hardware is not the Master) |
| 0 | Start state |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | SleepModeFrame |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | BusIdle timeout |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | "silent SleepMode" command (to reduce the BusIdle timeout) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | External Wakeup signal |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | Internal Wakeup signal |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Bus traffic (only occurs while the LIN hardware is not the Master) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 | Bus traffic (only occurs while the LIN hardware is not the Master) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Return Values | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.2 | LIN | • | • |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
