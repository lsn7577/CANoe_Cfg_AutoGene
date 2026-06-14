# J1939 Test Service Library Error Codes

> Category: `J1939` | Type: `notes`

## Description

-400

| Error Code | Description |
|---|---|
| 0 | Success |
| -1 | General Error |
| -2 | Resume due to constraint violation |
| -100 | Function cannot be called from a callback function |
| -101 | Invalid Handle |
| -102 | Invalid parameter |
| -103 | Cannot send request |
| -104 | Unknown environment variable |
| -105 | Environment variable has wrong type |
| -106 | Parameter exceeds range |
| -107 | Internal error |
| -108 | Node not found |
| -109 | Function can only be called from a callback function |
| -110 | ECU address not available |
| -111 | CAPL function not found |

| Error Code | Description |
|---|---|
| -200 | WaitPG-Data not available |
| -201 | Node is not a test node |
| -202 | ECU is offline |
| -203 | Timeout |
| -204 | Test pattern failed |
| -205 | Creation of a wait condition failed |
| -206 | No wait object available |
| -207 | Not all configured ACL messages received |
| -208 | Unexpected control byte in TPCM message |
| -209 | TPCM.CTS has requested to many packets |
| -210 | Wrong sequence number |
| -211 | Buffer too small |
| -212 | Unused byte is not equal 0xFF |

| Error Code | Description |
|---|---|
| -300 | Timeout CTS |
| -301 | Timeout Data |
| -302 | Timeout BAM |

| Error Code | Description |
|---|---|
| -400 | Cannot send message |

| Error Code | Description |
|---|---|
| -501 | Transport protocol error |
| -502 | Global Address not allowed |
| -503 | Abort from receiver |
| -504 | Abort form sender |
| -505 | Wrong sequence number |
| -506 | No connection free |
| -507 | Not possible with DLC <= 8 |
| -508 | Cannot initialize connection |
| -509 | No transport protocol available |
| -510 | Not possible with DLC <= 1785 |
| -511 | Transport protocol not available |
| -512 | Connection not found |
| -513 | Not possible with DLC > 223 |

| Version 15© Vector Informatik GmbH |
|---|
