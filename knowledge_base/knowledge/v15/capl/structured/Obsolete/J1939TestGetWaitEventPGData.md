# J1939TestGetWaitEventPGData

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by TestGetWaitJ1939PGData |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword J1939TestGetWaitEventPGData( pg pgBuffer, dword pgBufferSize ); |  |  |  |
| Function | If a message event is the last event that triggers a wait instruction, the message content can be called up with this function. |  |  |  |
| Parameters | pgBuffer buffer variable that should be filled in with this function |  |  |  |
| pgBufferSize size of buffer |  |  |  |  |
| Return Values | 0: Data access successful -1: Data access could not be executed, the last event was not a message event |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.1-8.2 SP2 | J1939 | — | • |  |
| Example long lret;pg EngineParameter engParam;lret = J1939TestWaitForPG(10, 0xFF, 0xF123, 500 );switch(lret) {case 1: if (J1939TestGetWaitEventPGData(engParam, elcount(engParam) ) == 0) { gValue = engParam.engineSpeed; } break;default: // error, timeout or constraint violation break;} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
