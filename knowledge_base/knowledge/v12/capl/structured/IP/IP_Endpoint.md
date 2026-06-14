# IP_Endpoint

> Category: `IP` | Type: `function`

## Syntax

```c
IP_Endpoint <endpoint> <var name>; // form 1
```

## Description

Initializes a variable of type IP_Endpoint with a concrete IP endpoint (form 1) or without an IP endpoint (form 2).

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

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| PortNumber Accesses the port number. The byte order is host byte order. | dword | — |
| IP_Address IP_Address object representing the IP_Endpoint's IP address. | IP_Address | — |
| IP_Address | CAPLfunctionIPAdredress.htm |  |
