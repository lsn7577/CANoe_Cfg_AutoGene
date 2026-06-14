# UdpReceiveFrom

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long UdpReceiveFrom( dword socket, char buffer[], dword size);
socket.ReceiveFrom( char buffer[], dword size);
```

## Description

The function receives data into the specified buffer. If the receive operation does not complete immediately the operation is performed asynchronously and the function will return SOCKET_ERROR (-1). Use IpGetLastSocketError to get a more specific error code. If the specific error code is WSA_IO_PENDING (997) the CAPL callback OnUdpReceiveFrom will be called on completion (successful or not), provided it is implemented in the same CAPL program.

## Return Values

0: The function completed successfully.

## Availability

| Since Version |
|---|
