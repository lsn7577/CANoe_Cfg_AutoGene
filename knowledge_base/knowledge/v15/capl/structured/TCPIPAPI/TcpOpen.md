# TcpOpen

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword TcpOpen( dword ipv4Address, dword port); // form 1
dword TcpOpen( byte ipv6Address[], dword port); // form 2
dword TcpOpen( IP_Endpoint localEndpoint ); // form 3
```

## Description

Depending on the address type, the function creates either an IPv4 or IPv6 TCP socket for use in connection-based, message-oriented communications. All parameters may be zero. If the port parameter is non-zero, the socket is implicitly bound to the given port. Otherwise the socket can be bound later on with IpBind or it will be automatically bound to a free port with TcpConnect.

Note:

If an address is given but the port is zero no implicit bind is performed. Please use IpBind after opening the socket in this case.

## Parameters

| Name | Description |
|---|---|
| ipv4Address | The numerical local IPv4 address to be used with the socket. If set to 0, then the socket is address unspecific (address wildcard). |
| ipv6Address | The local IPv6 address in a 16 byte array. Like in the IPv4 address an address wildcard can be retrieved using IpGetAddressAsArray(“::”, ipv6AddrArray). |
| port | The port in host-byte order to be used with the socket. If set to 0, then the socket is port unspecific (port wildcard). |
| localEndpoint | Bind the socket to this local endpoint. IP Address can be 0, if the socket should not be bound to an address. Port number can be undefined, if a dynamic port number should be used. Examples: IP_Endpoint(192.168.1.1:4000) – Bind to address and port IP_Endpoint(0.0.0.0:4000) – Bind only to port for IPv4 IP_Endpoint([::]:4000) – Bind only to port for IPv6 IP_Endpoint(192.168.1.1) – Bind to address and choose a dynamic port |

## Example

You can find further examples in the Ethernet chat sample configurations Open Folder (only with installed Ethernet option available).

```c
// ---------------------------------------------------
// start server
// ---------------------------------------------------
void serverStart()
{
  listenSocket = TcpOpen(0, listenPort);
  if (listenSocket != ~0)
  {
    if (TcpListen( listenSocket ) == 0)
    {
      // success…
    }
    else
    {
      writeLineEx(1, 3, " [ TcpListen: Error listening on socket. ]");
      TcpClose(listenSocket);
      listenSocket = ~0;
    }
  }
  else
  {
    writeLineEx( 1, 3, " [ TcpOpen: Error opening TCP Socket on port %d. (Error %d) ]", listenPort, IpGetLastError() );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: function/method 1-2 12.0: function/method 3 | 7.0: function 1-2 7.0 SP5: method 1-2 12.0: function/method 3 | 13.0 | 13.0: form 3 | — | 2.0 SP2: function/method 1-2 4.0: function/method 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
