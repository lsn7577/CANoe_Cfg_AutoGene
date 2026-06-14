# linChangeWakeupSettings

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by linSetWakeupBehavior |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword linChangeWakeupSettings(byte restartScheduler, long wakeupIdentifier) |  |  |  |
| Function | This function changes the wake-up setting. Note When LIN hardware is not in Sleep mode calling this function will have no effect. | Note When LIN hardware is not in Sleep mode calling this function will have no effect. |  |  |
| Note When LIN hardware is not in Sleep mode calling this function will have no effect. |  |  |  |  |
| Parameters | restartScheduler 0: After wake-up the current schedule table is started with the slot before entering sleep mode. 1: After wake-up the current schedule table is started from the beginning. In the case no schedule tables are defined this parameter is ignored. |  |  |  |
| wakeupIdentifier LIN frame identifier to be sent additionally directly after sending a wake-up signal. If an invalid identifier is specified i.e. not in the range 0..63: when schedule tables are defined no special wake-up identifier is sent; when no schedule tables are defined a SynchBreak / SynchField pair without an identifier is sent; Value range: 0..0xFF |  |  |  |  |
| Return Values | On success, a value unequal to zero, otherwise zero. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP4 | LIN | — | • |  |
| Example Change wake-up settings on getting Sleep mode event on linSleepModeEvent{linChangeWakeupSettings(0, 0x1); // do not restart scheduler, use 0x1 as wake-up identifier} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
