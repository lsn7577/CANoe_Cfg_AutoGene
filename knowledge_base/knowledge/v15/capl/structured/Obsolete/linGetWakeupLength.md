# linGetWakeupLength

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by linWakeupFrame selectors. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | int linGetWakeupLength (linWakeupFrame wakeupFrame) |  |  |  |
| Function | With this function it is possible to retrieve a length of an occurred Wakeup frame. |  |  |  |
| Parameters | wakeupFrame Bus-event of type LIN Wakeup frame. |  |  |  |
| Return Values | Returns the retrieved length [in units of 10 µsec] or zero on failure. |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.2 | LIN | • | • |  |
| Example Query the length of the wakeup frames on linWakeupFrame{write("Wake-up frame length: %d µs", linGetWakeupLength(this)*10);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
