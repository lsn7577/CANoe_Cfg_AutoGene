# IpGetAdapter

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword IpGetAdapter( long channel);
```

## Description

The function returns the index of the adapter which is attached to the given channel. For a VLAN adapter the channel and the vlanId has to be given.

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

| Since Version |
|---|
