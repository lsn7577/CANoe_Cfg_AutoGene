# IP_Address::PrintAddressToString

> Category: `IP` | Type: `method`

## Syntax

```c
long IP_Address::PrintAddressToString(char ipAddr[]);
```

## Description

Converts the IP address to a character string. In case of an IPv6 address the compressed IPv6 address notation is used. In this form the longest row of zeros will be replaced by two colons.

If the scope id in an IPv6 address is set to a value different than zero the address will be converted to the following form: <ipv6 address>%<scope id>

This scope ID should be set to the interface index in link local addresses.

Examples:

## Parameters

| Name | Description |
|---|---|
| ipAddr | String buffer where the string representing an IPv4 or IPv6 address is printed to. |

## Example

```c
on start
{
  IP_Address 192.168.1.1 addr;
  char addrStr[20];
  if (addr.PrintAddressToString( addrStr ) == 0)
  {
    write( "Address is %s", addrStr );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | 13.0 | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | Ethernet | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
