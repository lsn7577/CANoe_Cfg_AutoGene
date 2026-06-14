# linMrSchedSetGlobal

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Note This function may only be called in the event procedure on preStart. |  |  |  |  |
| Function Syntax | void linMrSchedSetGlobal(unsigned int cycleTime, unsigned int numberOfModes); |  |  |  |
| Function | Configures the basic parameters of the Scheduler. |  |  |  |
| Parameters | cycleTime Frequency with which the Scheduler works through its task lists. With a value of 0 it arranges the working steps directly after one another. Entries are made in milliseconds. |  |  |  |
| numberOfModes Number of individually configurable modes of the Scheduler. A maximal of 256 modes are allowed.During the measurement it is possible to switch between two modes with linMrSchedSetMode. |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.1 - 5.1 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
