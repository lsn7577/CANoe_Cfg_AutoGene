# IpGetAdapterVlanId

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterVlanId( dword ifIndex, word &retVlanId);
```

## Description

The function returns the VLAN ID of the adapter with the given index. If the adapter is not a VLAN interface it returns the error code WSA_INVALID_PARAMETER (87).

## Return Values

0: The function completed successfully.

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

| Since Version |
|---|
