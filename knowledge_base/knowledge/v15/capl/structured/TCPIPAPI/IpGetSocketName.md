# IpGetSocketName

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetSocketName( dword socket, dword &ipv4Address, dword &port); // form 1
long IpGetSocketName( dword socket, byte ipv6Address[], dword &port); // form 2
long IpGetSocketName( dword socket, IP_Endpoint localEndpoint ); // form 3
```

## Description

The function returns the local bound address and port of a socket.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| ipv4Address | The numerical IPv4 address is returned in this variable. |
| Ipv6Address | A 16 byte array to return the IPv6 address. |
| port | The local bound port. |
| localEndpoint | IP_Enpoint variable, where the address and port of the local endpoint is copied to. |

## Example

```c
on start
{
  LONG  ipv4SocketHandle;
  DWORD port;
  DWORD ipv4Address[1];
  CHAR  data[255];
  CHAR  addressStr[49];

  // open a IPv4 UDP socket. This will lead to an implicit bind
  ipGetAdapterAddress(1,ipv4Address, elcount(ipv4Address));
  ipv4SocketHandle = udpOpen(ipv4Address[0], 123);
  if(ipv4SocketHandle == ~0)
  {
    writeLineEx(1, 3, "%BASE_FILE_NAME%: failed to open the socket. Error code: %d", ipGetLastError());
  }

  // get the local bound address and port
  ipGetSocketName(ipv4SocketHandle, ipv4Address[0], port);
  ipGetAddressAsString(ipv4Address[0], addressStr, elcount(addressStr));
  writeLineEx(1, 1, "%BASE_FILE_NAME%: The IPv4 socket is bound to address %s and port %d", addressStr, port);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: function/method 1-2 12.0: function/method 3 | 8.2 SP2: function/method 1-2 12.0: function/method 3 | 13.0 | 13.0: form 3 | — | 2.0 SP2: function/method 1-2 4.0: function/method 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
