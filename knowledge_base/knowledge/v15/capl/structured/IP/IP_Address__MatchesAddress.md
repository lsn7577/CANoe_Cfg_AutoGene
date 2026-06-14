# IP_Address::MatchesAddress

> Category: `IP` | Type: `method`

## Syntax

```c
long IP_Address::MatchesAddress (IP_Address ipAddr); // form 1
long IP_Address::MatchesAddress (IP_Address ipAddr, long prefix); // form 2
```

## Description

Compares two addresses whereas wildcards matches always. If no address type is set or the address is set to 0.0.0.0 (IPv4) or ::0 (IPv6) this is considered as wildcard.

With form 2 only the network address of the IP address will be considered.

## Parameters

| Name | Description |
|---|---|
| ipAddr | An IP_Address object which may contain wildcards. |
| prefix | Prefix in number of bits. Only the first bits specified by prefix are considered. |

## Example

Example 1

Example 2

Example 3

```c
on start
{
  IP_Address 192.168.1.1 addr1;
  IP_Address 192.168.1.2 addr2;
  if (addr1.MatchesAddress( addr2 ) == 1)
  {
    write( "Address match!" );
  }
}
on start
{
  IP_Address 192.168.1.1 addr1;
  IP_Address 192.168.1.2 addr2;
  if (addr1.MatchesAddress( addr2, 24 ) == 1)
  {
    write( "Address match!" );
  }
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
| Since Version | 12.0 | 12.0 | 13.0 | 13.0: form 1 | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | Ethernet | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
