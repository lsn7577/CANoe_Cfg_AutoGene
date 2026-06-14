# J1939 Node Layer Error Codes

> Category: `J1939` | Type: `notes`

| Error Number | Error Code | Description | Additional Parameter inJ1939AppErrorIndication |
|---|---|---|---|
| 0001h | 000001h | Is not allowed to call this function from a callback. | — |
| 0002h | 000002h | Invalid Handle | — |
| 0004h | 000004h | Invalid Parameter | — |
| 0005h | 000005h | Request cannot be sent | — |
| 0006h | 000006h | Unknown Environment Variable | — |
| 0007h | 000007h | Wrong Environment Variable Type | — |
| 0008h | 000008h | Parameter exceeds range | — |
| 0080h | 000080h | Internal Error | — |
| 0100h | 000100h | General Error | — |
| 0201h | 000201h | Unknown bus name | — |
| 0202h | 000202h | ECU is offline | — |
| 0203h | 000203h | Invalid address | — |
| 0204h | 000204h | Sender and receiver ECUs are on different busses | — |
| 0206h | 000206h | Output PG only for local ECU allowed | — |
| 020Bh | 00020Bh | ECU is not initialized correctly | — |
| 020Ch | 00020Ch | Invalid node layer context | — |

| Error Number | Error Code | Description | Additional Parameter inJ1939AppErrorIndication |
|---|---|---|---|
| 1h | 010001h | CTS error - There was no CTS for an RTS. | PGN |
| 2h | 010002h | Data received after a timeout for a peer-to-peer connection | PGN |
| 3h | 010003h | Data received in the timeout during a BAM | — |

| Error Number | Error Code | Description | Additional Parameter inJ1939AppErrorIndication |
|---|---|---|---|
| 10h | 020010h | The node has received an Address Claiming from another node and had to relinquish its address for an ECU with higher priority. | — |

| Error Number | Error Code | Description | Additional Parameter inJ1939AppErrorIndication |
|---|---|---|---|
| 01h | 030001h | Error while sending a message | — |

| Error Number | Error Code | Description | Additional Parameter inJ1939AppErrorIndication |
|---|---|---|---|
| 30h | 040030h | Exception during protocol selection of BAM or CMDT | — |
| 40h | 040040h | Internal data buffer occupied | — |
| 60h | 040060h | User is sending a System PG via the CAPL interface | — |

| Error Number | Error Code | Description | Additional Parameter inJ1939AppErrorIndication |
|---|---|---|---|
| 1h | 050001h | An invalid sequence number is used | PGN |
| 70h | 050070h | A transfer with the transfer protocol was interrupted by the receiver. | PGN or 0 |
| 71h | 050071h | A transfer with the transfer protocol was interrupted by the sender. | PGN or 0 |
| 72h | 050072h | General transport protocol error | PGN |

| Version 15© Vector Informatik GmbH |
|---|
