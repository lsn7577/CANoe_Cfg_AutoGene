# GNSS Node Layer Error Codes: GNSSAppErrorIndication

> Category: `J1939` | Type: `notes`

| Error Code | Description |
|---|---|
| 0x01 | CTS error: There was no CTS for a RTS |
| 0x02 | The data was received after a timeout for a peer-to-peer connection. |
| 0x03 | The data received in the timeout during a BAM. |
| 0x04 | An EndOfMessage Acknowledge is missing or was received too late. |

| Error Code | Description |
|---|---|
| 0x10 | The node has received an Address Claiming from another node and has to release its address for an ECU with higher priority. |
| 0x15 | Initialization error: The ECU name was assigned twice. |
| 0x17 | Initialization error: The ECU address was assigned twice. It should be noted that this error is only reported if the same CAN channel is used in addition to the name or address used twice. |

| Error Code | Description |
|---|---|
| 0x30 | An exception occurred during the protocol selection of BAM or CMDT. |
| 0x40 | The internal data buffer is occupied already. |
| 0x60 | The user is sending a System PG via the GNSS CAPL interface. |

| Error Code | Description |
|---|---|
| 0x71 | A transfer with the transfer protocol was interrupted by the receiver (the parameter addInfo contains the PGN). |
| 0x72 | A transfer with the transfer protocol was interrupted by the sender (the parameter addInfo contains the PGN). |

| Version 15© Vector Informatik GmbH |
|---|
