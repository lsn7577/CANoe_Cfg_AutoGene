# IpLeaveMulticastGroup

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpLeaveMulticastGroup( dword socket, dword ifIndex, dword ipv4address ); // form 1
```

## Description

Leaves a previously joined multicast group on the given socket.

After that no multicast messages are received anymore.

To receive multicast messages, the multicast group has to be joined with IpJoinMulticastGroup before.

Before multicast messages can be sent, IpSetMulticastInterface has to be called before.

The function is dependent on the selected stack.

This functionality cannot be used in connection with the operating system TCP/IP stack.

## Return Values

0: The function completed successfully.

## Example

```c
variables
{
  UdpSocket gSocket;
}

on start
{
  gSocket = UdpSocket::Open( IP_Endpoint(0.0.0.0:40001) );
  gSocket.JoinMulticastGroup( 1, IP_Address(239.0.0.123) );
}

on key '2'
{
  gSocket.LeaveMulticastGroup( 1, IP_Address(239.0.0.123) );
}
```

## Availability

| Since Version |
|---|
