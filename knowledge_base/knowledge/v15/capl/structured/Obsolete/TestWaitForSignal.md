# TestWaitForSignal

> Category: `Obsolete` | Type: `notes`

## Description

TestWaitForSignals

| Deprecated Function Replaced by TestWaitForSignalAvailable. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestWaitForSignal (Signal aSignal, dword aTimeout) |  |  |  |
| Function | Tests the availability of a specific signal and waits if necessary until its availability.A signal that is received at least once from the bus after the measurement starts is classified as "available". This function is useful when you want to assure that single signals are available before starting a signal-oriented test, i.e. to synchronize the tester with the bus. |  |  |  |
| Parameters | aSignal Signal whose availability is being tested or for which is waited |  |  |  |
| aTimeout Maximum waiting time in ms. |  |  |  |  |
| Return Values | -2: Wait state is exited due to a constraint/condition violation |  |  |  |
| -1: General error, e.g. functionality is unavailable |  |  |  |  |
| 0: Wait state is exited due to a timeout |  |  |  |  |
| 1: Wait state is exited; signal is available for further tests |  |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
