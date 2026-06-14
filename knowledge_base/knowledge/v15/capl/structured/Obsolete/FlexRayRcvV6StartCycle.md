# FlexRayRcvV6StartCycle

> Category: `Obsolete` | Type: `notes`

| Deprecated Function This callback is deprecated and has been replaced by on FrStartCycle. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | FlexRayRcvV6StartCycle(long msgTime, byte nmlen, byte nmdata[]) |  |  |  |
| Function | A function defined in CAPL with this signature receives all FlexRay StartCycle events.The event is generated at the beginning of a communication cycle.It contains the NM vector that is valid for this round. |  |  |  |
| Parameters | msgTime Time stamp of the FlexRay frame. |  |  |  |
| nmlen Length of the NM vector. |  |  |  |  |
| Nmdata[] Network Management vector. |  |  |  |  |
| Return Values |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | FlexRay | • | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
