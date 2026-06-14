# AREthCloseEstablishedTCPConnection

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthCloseEstablishedTCPConnection (); // form 1
dword AREthCloseEstablishedTCPConnection (dword aepHandle); // form 2
dword AREthCloseEstablishedTCPConnection (dword aepHandle, dword remoteIPv4Address); // form 3
dword AREthCloseEstablishedTCPConnection (dword aepHandle, dword remoteIPv4Address, dword remotePort); // form 4
dword AREthCloseEstablishedTCPConnection (dword aepHandle, byte remoteIPv6Address[]); // form 5
long AREthCloseEstablishedTCPConnection (dword aepHandle, byte remoteIPv6Address[], dword remotePort); // form 6
long AREthCloseEstablishedTCPConnection (dword aepHandle, IP_Endpoint remoteIPEndpoint); // form 7
```

## Description

Closes one or multiple database defined TCP connection(s).

A TCP connection can be opened using the AREthEstablishTCPConnection function.

## Parameters

| Name | Description |
|---|---|
| aepHandle | Source application endpoint, which initiates the connection(s).Has to be defined in the database. |
| remotePort | Port on which the messages can be both sent and received. |
| remoteIPv4Address | IPv4 address to which the connection should be closed. IPv4 address can be converted with IPGetAdressAsNumber. |
| remoteIPv6Address | IPv6 address to which the connection should be closed. IPv6 address can be converted with IpGetAddressAsArray. |
| remoteIPEndpoint | Object of type IP_Endpoint that contains the address/port of the remote endpoint. |

## Example

```c
variables
{
  dword aep; // application Endpoint handle
}

on start
{
  // handle has to have a valid database application endpoint description
  aep = AREthOpenLocalApplicationEndpoint IP_Endpoint(TCP:192.168.1.1:40000));
}

on key 'o'
{ 
  // opens connection to specific endpoint
  if (AREthEstablishTCPConnection(aep, IP_Endpoint(TCP:192.168.1.2:50000)) != 0)
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0: form 1-6 12.0 SP2: form 7 | — | — | — | 2.2: form 1-6 4.0 SP2: form 7 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
