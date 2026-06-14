# linMrSendRequest

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by the function output. Such a call is only meaningful while a measurement is running. If no Slaves respond to a transmit request this leads to a LIN transmission error. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void linMrSendRequest(unsigned long requestId); |  |  |  |
| Function | When Master mode is activated this function sends a transmit request on the LIN bus for the specified LIN frame identifer. |  |  |  |
| Parameters | requestId 6 bit transmit identifier. |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.0 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
