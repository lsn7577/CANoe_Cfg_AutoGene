# GPIB Status

> Category: `GPIB` | Type: `notes`

## Description

Contains the status bits of the current bus/device situation.Integer, 2 Bytes

| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ERR | TIMO | END | SRQI | RQS | — | — | CMPL | LOK | REM | CIC | ATN | TACS | LACS | DTAS | DCAS |

| ERR | Error detected |
|---|---|
| TIMO | Timeout |
| END | EOI or EOS detected |
| SRQI | SRQ detected by CIC |
| RQS | Device needs service |
| CMPL | I/O completed |
| LOK | Local lockout state |
| REM | Remote state |
| CIC | Controller-in-Charge |
| ATN | Attention asserted |
| TACS | Talker active |
| LACS | Listener active |
| DTAS | Device trigger state |
| DCAS | Device clear state |

| Version 15© Vector Informatik GmbH |
|---|
