# IpGetAdapterVlanId

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterVlanId( dword ifIndex, word &retVlanId);
```

## Description

The function returns the VLAN ID of the adapter with the given index. If the adapter is not a VLAN interface it returns the error code WSA_INVALID_PARAMETER (87).

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. |
| retVlanId | The VLAN ID of the adapter. |

## Example

```c
on start
{
  dword adapterCount;
  dword ifIndex;
  word vlanId;
  long result;
  adapterCount = ipGetAdapterCount();

  for(ifIndex = 1; ifIndex <= adapterCount; ifIndex++)
  {
    result = ipGetAdapterVlanId(ifIndex, vlanId);
    if(result == 0)
    {
      write("Adapter %d has VLAN id %d", ifIndex, vlanId);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
