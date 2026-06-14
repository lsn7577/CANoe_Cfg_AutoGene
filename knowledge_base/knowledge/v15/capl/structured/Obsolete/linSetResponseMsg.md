# linSetResponseMsg

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by the function output. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long linSetResponseData(message msg); |  |  |  |
| long linSetResponseMsg(message msg, byte checksum); |  |  |  |  |
| Function | Sets the response data for a transmit request. The LIN hardware is instructed to immediately respond to the transmit request with the same identifier as msg with the data bytes of msg. When you use the first alternative of the syntax (see above), the checksum is automatically generated correctly. When you use the second alternative of the syntax (see above), you can set any checksum. If this function is called in the event procedure on preStart then the LIN hardware is configured so that the response is made to a suitable transmit request. During the measurement this method may only be called for transmit identifiers that were already configured in the event procedure on preStart or in the LIN database. |  |  |  |
| Parameters | msg Pattern for the transmitting behavior of the LIN hardware. In the future, in response to the transmit identifier that is defined by this message, the data bytes of this message will be sent.In general msg will be a message contained in the database created for LIN. This offers an easy way to access the individual signal values. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.0 | LIN | — | • |  |
| Example message LinSlaveLeft sLinSlaveLeft;sLinSlaveLeft.Angle = 50;linSetResponseMsg(sLinSlaveLeft); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
