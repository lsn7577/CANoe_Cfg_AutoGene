# IpSetSocketOption

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpSetSocketOption( dword socket, long level, long name, long value); // form 1
socket.SetSocketOption( long level, long name, long value); // form 1
```

## Description

The function modifies a socket option.

The function is dependent on the selected stack.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  CHAR errorMessage[255];
  LONG tcpSocket;
  LONG result;
  LONG value;

  // open a tcp socket
  tcpSocket = tcpOpen(0,0);
  if( tcpSocket == ~0 )
  {
    write("open tcp socket failed. Last error was %d", ipGetLastError());
  }

  // activate SO_KEEPALIVE on the tcp socket
  result = ipSetSocketOption(tcpSocket, "SOL_SOCKET", "SO_KEEPALIVE", 1);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
    write("Failed to set socket option SO_KEEPALIVE. Error: %s", errorMessage);
  }

  // set Time to live it is greater than 32
  result = ipGetSocketOption(tcpSocket, "IPPROTO_IP", "IP_TTL", value);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option IP_TTL. Error: %s", errorMessage);
  }
  if( value > 32 )
  {
    result = ipSetSocketOption(tcpSocket, "IPPROTO_IP", "IP_TTL", 32);
    if( result != 0 )
    {
      ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
      write("Failed to set socket option IP_TTL. Error: %s", errorMessage);
    }
  }

  // avoid tcp to use the nagle algorithm
  result = ipSetSocketOption(tcpSocket, "IPPROTO_TCP", "TCP_NODELAY", 1);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option TCP_NODELAY. Error: %s", errorMessage);
  }

  // connect the socket
  result = tcpConnect(tcpSocket, IpGetAddressAsNumber("192.168.1.2"), 21);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(tcpSocket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option TCP_NODELAY. Error: %s", errorMessage);
  }
}
```

## Availability

| Since Version |
|---|
