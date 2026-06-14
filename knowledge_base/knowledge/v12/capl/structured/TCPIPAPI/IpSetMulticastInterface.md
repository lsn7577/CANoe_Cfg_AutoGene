# IpSetMulticastInterface

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpSetMulticastInterface ( dword socket, dword ifIndex );
```

## Description

Set the interface for outgoing multicast messages. Without calling this no multicast messages can be sent on the given socket.

To receive multicast messages, the multicast group has to be joined with IpJoinMulticastGroup before.

To leave a multicast group, call IpLeaveMulticastGroup.

The function is dependent on the selected stack.

This functionality cannot be used in connection with the operating system TCP/IP stack.

## Return Values

0: The function completed successfully.

## Example

```c
variables
{
  const dword IPV4_STR_SIZE = 16;            // IPv4 string size
  const dword INVALID_SOCKET = ~0;           // invalid socket constant
  dword udpMulticastSocket = INVALID_SOCKET; // a multicast socket
  dword port = 12345;                        // port to send udp to.
  dword ifIdx = 1;                           // interface index.
  dword ipv4MulticastAddr;                   // an IPv4 multicast address
  char ipv4MulticastAddrStr[IPV4_STR_SIZE] = "224.123.111.222"; // an IPv4 multicast address
}

on start
{
  long result; // function result
  // calculate the numeric multicast address.
  ipv4MulticastAddr = IpGetAddressAsNumber( ipv4MulticastAddrStr );

  udpMulticastSocket = UdpOpen(0, 0); // open an UDP socket...
  if (udpMulticastSocket != INVALID_SOCKET)
  {
    result = IpSetMulticastInterface( udpMulticastSocket, ifIdx );
    if (result == 0)
    {
      write("Socket %d set to send multicast %s on adapter %d.", udpMulticastSocket, ipv4MulticastAddrStr, ifIdx);
      write("Sending some multicast messages to %s:%d ...", ipv4MulticastAddrStr, port);
      UdpSendTo( udpMulticastSocket, ipv4MulticastAddr, port, "a", 1 );
      UdpSendTo( udpMulticastSocket, ipv4MulticastAddr, port, "b", 1 );
      UdpSendTo( udpMulticastSocket, ipv4MulticastAddr, port, "c", 1 );
    }
    else
    {
      writeLineEx(1, 3, "IpSetMulticastInterface: Error %d", result);
    }
  }
  else
  {
    writeLineEx( 1, 3, "UdpOpen: Failed to open socket.");
  }
}

on preStop
{
  // close the socket
  UdpClose(udpMulticastSocket);
}
```

## Availability

| Since Version |
|---|
