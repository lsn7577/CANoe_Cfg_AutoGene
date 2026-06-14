# AREthCloseEstablishedTCPConnection

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthCloseEstablishedTCPConnection (); // form 1
```

## Description

Closes one or multiple database defined TCP connection(s).

A TCP connection can be opened using the AREthEstablishTCPConnection function.

## Return Values

0: The function was successfully executed

## Example

```c
variables
{
  dword aep; // application Endpoint handle
  dword tcp = 6;
  dword clientIP; // numerical representation of client IP
  dword clientPort = 40000; // TCP client port
  dword serverIP; // numerical representation of server IP
  dword serverPort = 50000; // TCP server port
}

on start
{
  clientIP = ipGetAddressAsNumber("192.168.1.1");
  serverIP = ipGetAddressAsNumber("192.168.1.2");
  // handle has to have a valid database application endpoint description
  aep = AREthOpenLocalApplicationEndpoint(tcp, clientPort, clientIP);
}

on key 'o'
{ 
  // opens connection to specific endpoint
  if (AREthEstablishTCPConnection(aep, serverIP, serverPort) != 0)
  {
    write("connection not established");
  }
}

on key 'c'
{
  // close all connections within node context
  if (AREthCloseEstablishedTCPConnection () == 0)
  {
    write("connection(s) closed");
  }
}
```

## Availability

| Since Version |
|---|
