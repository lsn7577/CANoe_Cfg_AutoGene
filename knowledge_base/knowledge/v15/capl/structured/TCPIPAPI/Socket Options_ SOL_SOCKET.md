# Socket Options: SOL_SOCKET

> Category: `TCPIPAPI` | Type: `notes`

## Description

The following socket options can be set at the SOL_SOCKET option level in CAPL. They influence the behavior of the socket. For all BOOL typed options a non-zero value will be interpreted as TRUE.

See Also

| Socket Option | Set/Get | Description | Type | Stack |
|---|---|---|---|---|
| SO_DEBUG | set/get | Activates the recording of debugging information. CANoe currently do not output any debug information. | DWORD (boolean) | C/W |
| SO_ACCEPTCONN | get | Returns if a socket is in listening mode. This only works for connection orientated protocols like TCP. | DWORD (boolean) | C/W |
| SO_REUSEADDR | set/get | Allow local address and port reuse. But even if two sockets are bound to the same port the behavior which socket receives the packet is undefined. | DWORD (boolean) | C/W |
| SO_KEEPALIVE | set/get | Enables keep connections alive for a socket connection. Only valid for connection orientated protocols like TCP. The default keep alive timeout is 2 hours. | DWORD (boolean) | C/W |
| SO_DONTROUTE | set/get | If this option is enabled, the socket can only send in a local network. The routing to the default gateway is disabled. | DWORD (boolean) | C/W |
| SO_BROADCAST | set/get | Enable sending broadcast data on a socket. This option is only valid for UDP sockets. The option set by default during udpOpen. | DWORD (boolean) | C/W |
| SO_OOBINLINE | set/get | Activates the reception of out-of-band data in band. This option is only allowed on TCP sockets. | DWORD (boolean) | C/W |
| SO_SNDBUF | set/get | Set the size of the buffers for outgoing data. | DWORD | C/W |
| SO_RCVBUF | set/get | Set the size of the buffers for incoming data. | DWORD | C/W |
| SO_SNDLOWAT | set/get | Set the minimum count of data for output. | DWORD | C |
| SO_RCVLOWAT | set/get | Set the minimum count of data for input. | DWORD | C |
| SO_SNDTIMEO | set/get | Set the timeout value in ms for blocking send calls. | DWORD | C/W |
| SO_RCVTIMEO | set/get | Set the timeout value in ms for blocking receive calls. | DWORD | C/W |
| SO_ERROR | get | Get the last error code on this socket. | DWORD | C/W |
| SO_TYPE | get | Returns the socket type of this socket. For UDP sockets 2 is returned. For TCP sockets 1 is returned. | DWORD | C/W |
| SO_EXCLUSIVEADDRUSE | set/get | If this option is set its not possible for any other socket to bind to the same address and port. | DWORD | W |
| SO_DONTLINGER | set/get | If option is set to 0 a connected socket will abort immediately. If option is set to 1 a connected socket will send all pending data first and will then initiate the shutdown sequence. On a windows socket the port will be unavailable for new socket connections until the socket moves from TIME_WAIT state to CLOSED state. | DWORD | C/W |

| Version 15© Vector Informatik GmbH |
|---|
