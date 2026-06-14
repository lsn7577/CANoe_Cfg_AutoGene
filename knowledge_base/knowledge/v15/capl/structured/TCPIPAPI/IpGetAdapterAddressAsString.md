# IpGetAdapterAddressAsString

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterAddressAsString( dword ifIndex, char address[], dword count);
```

## Description

The function retrieves the string representation of the first address associated with the specified network interface.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| address | The buffer used to store the address string in dot notation. |
| count | The size of the address buffer. |

## Example

```c
on start
{
  const dword IPV4_STR_SIZE = 16; // IPv4 string size
  char ipAddr[IPV4_STR_SIZE];     // human readable ipv4 address string.
  dword ifIdx;                    // interface index
  long result;                    // function result.

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    result = IpGetAdapterAddressAsString( ifIdx, ipAddr, elcount(ipAddr) );
    if (result == 0)
    {
      // success.
      write("IpGetAdapterAddressAsString for adapter %d returned: %s", ifIdx, ipAddr);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterAddressAsString: Error %d", result);
      // handle error...
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
