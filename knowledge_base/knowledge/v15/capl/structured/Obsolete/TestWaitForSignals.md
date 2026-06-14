# TestWaitForSignals

> Category: `Obsolete` | Type: `notes`

## Description

TestWaitForSignal

| Deprecated Function Replaced by TestWaitForSignalsAvailable. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestWaitForSignals (dbNode aNode, dword aTimeout) |  |  |  |
| Function | Tests the availability of all the send signals of a node and waits if necessary until all the send signals of the node are available. Signals that are received at least once from the bus after the measurement starts are classified as "available". This function is useful when you want to assure that all signals are available before starting a signal-oriented test, i.e. to synchronize the tester with the bus. |  |  |  |
| Parameters | aNode Node whose send signals should all be available |  |  |  |
| aTimeout [ms] Maximum waiting time |  |  |  |  |
| Return Values | -2: Wait state is exited due to a constraint/condition violation |  |  |  |
| -1: General error, e.g. functionality is unavailable |  |  |  |  |
| 1: General error, e.g. functionality is unavailable |  |  |  |  |
| 0: Wait state is exited due to a timeout; not all signals are available |  |  |  |  |
| 1: The wait state is exited; all of the node’s send signals are available for further tests |  |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
