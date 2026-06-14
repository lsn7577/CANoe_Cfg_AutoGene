# IpGetSocketOption

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetSocketOption( dword socket, char level[], char name[], long &value);
socket.GetSocketOption(char level[], char name[], long &value);
```

## Description

The function reads the value of the given socket option.

The function is dependent on the selected stack.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  char errorMessage[255];
  long socket;
  long result;
  long value;

  // open a udp socket
  socket = udpOpen(0,0);
  if( socket == ~0 )
  {
    write("open udp socket failed. Last error was %d", ipGetLastError());
  }
  
  // get the socket type (UDP = 2, TCP = 1)
  result = ipGetSocketOption(socket, "SOL_SOCKET", "SO_TYPE", value);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(socket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option SO_TYPE. Error: %s", errorMessage);
  }
  else
  {
    write("The socket type is %d", value);
  }
  result = ipGetSocketOption(socket, "IPPROTO_IP", "IP_TTL", value);
  if( result != 0 )
  {
    ipGetLastSocketErrorAsString(socket, errorMessage, elcount(errorMessage));
    write("Failed to get socket option IP_TTL. Error: %s", errorMessage);
  }
  else
  {
    write("The IP TTL of this socket is %d", value);
  }
}
```

## Availability

| Since Version |
|---|
