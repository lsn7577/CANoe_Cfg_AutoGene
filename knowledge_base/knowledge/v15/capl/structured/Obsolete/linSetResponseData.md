# linSetResponseData

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by the function output. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long linSetResponseData(int sendId, int dataLength, byte data[]); |  |  |  |
| long linSetResponseData(int sendId, int dlc, byte data[], byte checksum); |  |  |  |  |
| Function | Sets the response data for a transmit request. The LIN hardware is instructed to respond from now on to the transmit request sendID with the data data. The used data length code is passed in dlc. If no DLC has been set by the data base, the DLC will be set by the dlc parameter of the function. If the DLC already has been set by the data base, this value must be handover correctly on every call of this function. The functionality to set the DLC is only available with LIN specification 1.2 (or above)! LIN specification 1.1 presets the DLC of an identifier. DLC value range: 0…8 (bytes)When you use the first alternative of the syntax (see above), the checksum is automatically generated correctly. When you use the second alternative of the syntax (see above), you can set any checksum. If this function is called in the event procedure on preStart then the LIN hardware is configured so that the response is made to a suitable transmit request. During the measurement this method may only be called for transmit identifiers that were already configured in the event procedure on preStart or in the LIN database. |  |  |  |
| Parameters | sendId Transmit identifier to which this call refers. |  |  |  |
| dlc DLC of the message |  |  |  |  |
| data Data bytes which should be sent immediately upon a sendId requests. |  |  |  |  |
| checksum Checksum that has to be used |  |  |  |  |
| Return Values | If a DLC has been set, a value unequal "0" will be returned. |  |  |  |
| If no DLC has been set, the value "0" will be returned. |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.0 | LIN | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
