# linMrSchedSetRqId

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Note This function may only be called in the event procedure on preStart. |  |  |  |  |
| Function Syntax | void linMrSchedSetRqId (unsigned int requestId, unsigned long period, unsigned char modeFlags[]); |  |  |  |
| Function | Creates an entry for the Scheduler. Note linMrSchedSetRqId may only be called once for each LIN Message Identifier. During a processing step of the Scheduler the outstanding transmit requests are serviced in the order in which they were configured by linMrSchedSetRqId. | Note linMrSchedSetRqId may only be called once for each LIN Message Identifier. During a processing step of the Scheduler the outstanding transmit requests are serviced in the order in which they were configured by linMrSchedSetRqId. |  |  |
| Note linMrSchedSetRqId may only be called once for each LIN Message Identifier. During a processing step of the Scheduler the outstanding transmit requests are serviced in the order in which they were configured by linMrSchedSetRqId. |  |  |  |  |
| Parameters | requestId LIN Message Identifier for which transmit requests should be placed. |  |  |  |
| period Regulates the frequency of the request. The duration between two requests is the period * cycle time of the Scheduler. |  |  |  |  |
| modeFlags Bit field that must be large enough to take up a bit for each Scheduler mode.The least significant bit of Byte 0 refers to Mode 0, the least significant bit of Byte 1 refers to Mode 8, etc.One entry is made for each mode for which a corresponding flag is set. |  |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.1 - 5.1 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
