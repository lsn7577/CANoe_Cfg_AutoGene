# IpSetAdapterMacId

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpSetAdapterMacId( dword ifIndex, qword macId);
```

## Description

Sets the mac id of the given interface.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters. All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| macId | The MAC address as qword. |

## Example

```c
on start
{
  dword result;
  dword channel = 1;
  dword ifIndex;
  qword macId;

  ifIndex = ipGetAdapter(channel);
  if(ifIndex > 0)
  {
    macId = ethGetMacAddressAsNumber("02:11:22:33:44:55");
    result = ipSetAdapterMacId(ifIndex, macId);
    if(result != 0)
    {
      write("ipSetAdapterMacId for interface %d failed", ifIndex);
    }
  }
  else
  {
    write("No interface found for channel %d", channel);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 13.0 | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
