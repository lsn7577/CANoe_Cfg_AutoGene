# IP_Endpoint

> Category: `IP` | Type: `function`

## Syntax

```c
IP_Endpoint(192.168.1.2:4001);
```

## Description

Initializes a variable of type IP_Endpoint with a concrete IP endpoint (form 1) or without an IP endpoint (form 2).

## Parameters

| Name | Description |
|---|---|
| endpoint | An IPv4 or IPv6 address and port number separated by a colon. |
| var name | Character string defining the object's variable name. |

## Example

```c
variables
{
  IP_Endpoint TCP:192.168.1.1:4000 ipEndpoint1;
  IP_Endpoint 192.168.1.2:4001     ipEndpoint2;
  IP_Endpoint 192.168.1.2          ipEndpoint3;
  IP_Endpoint UDP:[ff::1]:6000     ipEndpoint4;
  IP_Endpoint [ff::1]:6001         ipEndpoint5;
  IP_Endpoint ff::1                ipEndpoint6;
}
on start
{
  IP_Endpoint ep;
  ep = IP_Endpoint(192.168.1.2:4001);
  // ... do something with ep
}
on start
{
  DoSomething( IP_Address(FC00::0001) );
}

void DoSomething( IP_Address addr )
{
  if (addr.IsIPv4Address())
  {
    // ...
  }
  else if (addr.IsIPv6Address())
  {
    // ...
  }
}
on start
{
  IP_Endpoint 192.168.1.1:4000 ep1;
  IP_Endpoint 192.168.1.1:4000 ep2;
  if (ep1 == ep2)
  {
    write( "Endpoints are equal!" );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
