# IpGetAdapterVlanDefaultPriority

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterVlanDefaultPriority( dword ifIndex, word &retVlanDefaultPriority);
```

## Description

The function returns the VLAN priority of the adapter with the given index. If the adapter is not a VLAN interface it returns the error code WSA_INVALID_PARAMETER (87).

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  dword adapterCount;
  dword ifIndex;
  word prio;
  long result;
  adapterCount = ipGetAdapterCount();

  for(ifIndex = 1; ifIndex <= adapterCount; ifIndex++)
  {
    result = IpGetAdapterVlanDefaultPriority (ifIndex, prio);
    if(result == 0)
    {
      write("Adapter %d has VLAN priority %d", ifIndex, prio);
    }
  }
}
```

## Availability

| Since Version |
|---|
