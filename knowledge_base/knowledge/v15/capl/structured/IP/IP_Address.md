# IP_Address

> Category: `IP` | Type: `function`

## Syntax

```c
IP_Address(192.168.1.1);
IP_Address(192.168.1.1) );
```

## Description

Initializes a variable of type IP_Address with a concrete IP address (form 1) or without an IP Address (form 2).

## Parameters

| Name | Description |
|---|---|
| addr | An IPv4 or IPv6 address. |
| var name | Character string defining the object's variable name. |

## Example

```c
variables
{
  IP_Address 192.168.0.1 ipv4Addr;
  IP_Address ff::1       ipv6Addr;
  IP_Address [ff::2]     ipv6Addr2;
  IP_Address 0.0.0.0     ipv4AnyAddr;
  IP_Address ::          ipv6AnyAddr;
}
on start
{
  IP_Address addr;
  addr = IP_Address(192.168.1.1);
  // ... do something with addr
}
on start
{
  DoSomething( IP_Address(192.168.1.1) );
}

void DoSomething( IP_Address addr )
{
  // ... do something with addr
}
on start
{
  IP_Address 192.168.1.1 addr1;
  IP_Address 192.168.1.2 addr2;
  if (addr1 == addr2)
  {
    write( "Addresses are equal!" );
  }
  else
  {
    write( "Addresses are not equal!" );
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
