# IpGetAdapterChannel

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterChannel( dword ifIndex);
```

## Description

The function returns the number of the Ethernet channel (1 for Eth 1) to which the network adapter with the given index is attached.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. |

## Return Values

The Ethernet channel number or 0 if the given ifIndex was invalid.

## Example

```c
on start
{
  dword adapterCount;
  dword ifIndex;
  long channel;
  adapterCount = ipGetAdapterCount();

  for(ifIndex = 1; ifIndex <= adapterCount; ifIndex++)
  {
    channel = IpGetAdapterChannel (ifIndex);
    if(channel != 0)
    {
      write("Adapter %d is attached to channel %d", ifIndex, channel);
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
