# IpGetAddressAsNumber

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword IpGetAddressAsNumber( char address[]);
```

## Description

The function converts an IPv4 address string in dot notation to it's numerical value in network-byte order.

## Parameters

| Name | Description |
|---|---|
| address | The numerical IPv4 address to be converted. |

## Return Values

4294967295 (0xFFFFFFF, the equivalent of "255.255.255.255"): The specified address string was invalid.

## Example

```c
on start
{
  const dword IPV4_STR_SIZE = 16;    // IPv4 string size
  char ipv4AddrStr[IPV4_STR_SIZE] = "129.168.111.222";

  write("Converting IPv4 Address %s to numerical value => 0x%x", ipv4AddrStr, IpGetAddressAsNumber(ipv4AddrStr));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ ( since version 11.0) | ✔ ( since version 11.0) | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
