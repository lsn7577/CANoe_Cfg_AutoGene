# IpGetAddressAsArray

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword IpGetAddressAsArray( char address[], byte ipv6Address[]);
```

## Description

The function converts an address string in colon notation to a 16 byte array with the address bytes in network order.

## Parameters

| Name | Description |
|---|---|
| address | The numerical IPv4 address to be converted. |
| ipv6Address | The array used to store the converted IPv6 address as 16 byte array. |

## Example

```c
on start
{
  const dword IPV6_STR_SIZE = 40; // IPv6 string size
  int i;                          // loop variable
  byte ipv6Addr[16];              // IPv6 address bytes.
  dword result;                   // function result

  char ipv6AddrStr[IPV6_STR_SIZE] = "2001:DB8:85A3:8D3:1319:8A2E:370:7344";

  write("Converting IPv6 Address %s to bytes...", ipv6AddrStr);

  result = IpGetAddressAsArray( ipv6AddrStr, ipv6Addr );
  if (result == 0)
  {
    // success...
    write("IpGetAddressAsArray: returned array with IPv6 bytes:");
    for ( i=0; i<16; i++)
    {
      write("Byte %.2d = 0x%.2x", i, ipv6Addr[i]);
    }
  }
  else
  {
    writeLineEx(1, 3, "IpGetAddressAsArray: The specified address string was invalid.");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.0 | 13.0 | 13.0 | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ ( since version 11.0) | ✔ ( since version 11.0) | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
