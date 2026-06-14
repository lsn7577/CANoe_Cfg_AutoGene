# FlexRayRcvV6Frame

> Category: `Obsolete` | Type: `notes`

| Deprecated Function This callback is deprecated and has been replaced by on FrFrame. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | FlexRayRcvV6Frame( long msgTime, word channel, word frameID, byte cycle, byte len, byte data[], int sync, int NMIndication, int ReservedFlag, word headerCRC, word status, int rcv ) |  |  |  |
| Function | A function defined in CAPL with this signature receives all FlexRay frames. |  |  |  |
| Parameters | msgTime Time stamp of the FlexRay frame. |  |  |  |
| channel Channel of the send messageValue: 1 or 2. |  |  |  |  |
| frameID Identifier of message to be sent, identifies the time window. |  |  |  |  |
| cycle Current cycle. |  |  |  |  |
| len Number of data bytes (Maximum 64 bytes). |  |  |  |  |
| data[] Data bytes. |  |  |  |  |
| sync Sync Flag.Indicates whether this message is used for time synchronization. |  |  |  |  |
| NMIndication Network Management Bit.When this bit is set the first two data bytes contain the local NM vector. |  |  |  |  |
| ReservedFlag — |  |  |  |  |
| headerCRC Checksum of the header. |  |  |  |  |
| status Status field of the message. |  |  |  |  |
| rcv Send direction: 1 TX 0 RX | 1 | TX | 0 | RX |
| 1 | TX |  |  |  |
| 0 | RX |  |  |  |
| Return Values |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | FlexRay | • | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
