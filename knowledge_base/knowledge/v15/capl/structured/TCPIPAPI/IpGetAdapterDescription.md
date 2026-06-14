# IpGetAdapterDescription

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterDescription( dword ifIndex, char name[], dword count);
```

## Description

The function retrieves the description of the specified network interface.

All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. |
| name | The buffer used to store the description. |
| count | The size of the name buffer. |

## Example

```c
on start
{
  const dword STR_SIZE = 256; // string buffer size
  char ifDescr[STR_SIZE];     // Interface description string.
  dword ifIdx;                // interface index
  long result;                // function result.

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    result = IpGetAdapterDescription( ifIdx, ifDescr, elcount(ifDescr) );
    if (result == 0)
    {
      // success.
      write("IpGetAdapterDescription for adapter %d returned: %s", ifIdx, ifDescr);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterDescription: Error %d", result);
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
