# linInitSetBaseBaud

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Note This function may only be called in the event procedure on preStart. |  |  |  |  |
| Function Syntax | void linInitSetBaseBaud(long baudrate); |  |  |  |
| Function | Sets the transmission speed in baud on the LIN bus. This overwrites the value from the LIN database. |  |  |  |
| Parameters | baudrate Permitted are values from 0,2 - 20 kBaud. The default value is 9600 Baud. Baud rates < 1 kBaud are not LIN compliant. |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.1 - 5.1 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
