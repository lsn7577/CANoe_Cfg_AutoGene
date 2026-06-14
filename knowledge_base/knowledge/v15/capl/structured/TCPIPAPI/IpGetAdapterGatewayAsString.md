# IpGetAdapterGatewayAsString

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterGatewayAsString( dword ifIndex, char address[], dword count);
```

## Description

The function retrieves the string representation of the default gateway address associated with the specified network interface.

Gateway information is not yet available before the start of the measurement (on pre-start). Rather it is first available at the start of the measurement (on start) as soon as the stack has been completely initialized.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| address | The buffer used to store the gateway IPv4 address string in dot notation. |
| count | The size of the address buffer. |

## Example

```c
on start
{
  const dword IPV4_STR_SIZE = 16;    // IPv4 string size
  dword ifIdx;                       // interface index
  char ipv4GwAddrStr[IPV4_STR_SIZE]; // human readably IPv4 Gateway address.
  long result;                       // function result.

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    result = IpGetAdapterGatewayAsString( ifIdx, ipv4GwAddrStr, elcount(ipv4GwAddrStr) );
    if (result == 0)
    {
      // success.
      write("IpGetAdapterGatewayAsString for adapter %d returned IPv4 gateway address: %s", ifIdx, ipv4GwAddrStr);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterGatewayAsString: Error %d", result);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
