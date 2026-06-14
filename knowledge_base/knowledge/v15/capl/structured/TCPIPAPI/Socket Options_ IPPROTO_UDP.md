# Socket Options: IPPROTO_UDP

> Category: `TCPIPAPI` | Type: `notes`

## Description

The following socket options can be set at the IPPROTO_UDP socket option level in CAPL. They influence the behavior of the UDP protocol per socket. For all BOOL typed options a non-zero value will be interpreted as TRUE.

UDP_NOCHECKSUM

set/get

See Also

| Socket Option | Set/Get | Description | Type | Stack |
|---|---|---|---|---|
| UDP_NOCHECKSUM | set/get | The UDP checksum will be set to zero if this option is set TRUE. | DWORD (boolean) | W |

| Version 15© Vector Informatik GmbH |
|---|
