# IpGetAdapterChannel

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterChannel( dword ifIndex);
```

## Description

The function returns the number of the Ethernet channel (1 for Eth 1) to which the network adapter with the given index is attached.

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

| Since Version |
|---|
