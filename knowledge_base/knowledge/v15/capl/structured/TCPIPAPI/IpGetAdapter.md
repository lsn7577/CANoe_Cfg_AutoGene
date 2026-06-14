# IpGetAdapter

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword IpGetAdapter( long channel); // from 1
dword IpGetAdapter( long channel, word vlanId); // from 2
```

## Description

The function returns the index of the adapter which is attached to the given channel. For a VLAN adapter the channel and the vlanId has to be given.

## Parameters

| Name | Description |
|---|---|
| channel | The 1-based Ethernet channel index. |
| vlanId | The VLAN id of the adapter. |

## Return Values

The adapter index or 0 if there is no adapter for the given channel or VLAN available.

## Example

```c
variables
{
const long kMAX_CHANNEL = 64;
const word kMAX_VLAN = 4094;
}

on start
{
  long channel;
  word vlanId;
  word prio;
  dword ifIndex;

  for(channel = 1; channel <= kMAX_CHANNEL; channel++)
  {
    ifIndex = IpGetAdapter(channel);
    if(ifIndex > 0)
    {
      write("Index of channel %d adapter: %d", channel, ifIndex);
      for(vlanId = 1; vlanId <= kMAX_VLAN; vlanId++)
      {
        ifIndex = IpGetAdapter(channel, vlanId);
        if(ifIndex > 0)
        {
          write("Index of vlan %d = %d", vlanId, ifIndex );
        }
      }
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
