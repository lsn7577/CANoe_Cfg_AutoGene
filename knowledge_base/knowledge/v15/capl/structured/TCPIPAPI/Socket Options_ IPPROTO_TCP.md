# Socket Options: IPPROTO_TCP

> Category: `TCPIPAPI` | Type: `notes`

## Description

The following socket options can be set at the IPPROTO_TCP socket option level in CAPL. They influence the behavior of the TCP protocol per socket. For all BOOL typed options a non-zero value will be interpreted as TRUE.

See Also

| Socket Option | Set/Get | Description | Type | Stack |
|---|---|---|---|---|
| TCP_NODELAY | set/get | The Nagle algorithm for TCP sockets will be disabled if this option is set to a non-zero value. The Nagle algorithm collects small amounts of output data to send in a single packet if outstanding data has not yet been acknowledged. | DWORD (boolean) | C/W |
| TCP_MAXSEG | C:set/get W: get | The maximum segment size is normally negotiated between sender and receiver. This option allows to check the result of this operation and to reduce it. | DWORD | C/W |
| TCP_NOOPT | set/get | Avoid the TCP protocol to send TCP options. | DWORD (boolean) | C |
| TCP_NOPUSH | set/get | Normally the push flag is set and the data is send immediately on the end of every user call to TcpSend. When the option is set to a non-zero value, TCP will delay sending any data until either the socket is closed, or the internal send buffer is filled. | DWORD (boolean) | C |

| Version 15© Vector Informatik GmbH |
|---|
