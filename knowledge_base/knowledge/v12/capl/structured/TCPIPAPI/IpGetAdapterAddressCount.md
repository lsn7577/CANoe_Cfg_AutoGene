# IpGetAdapterAddressCount

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterAddressCount( dword ifIndex, dword addressFamily);
```

## Description

The function returns the count of addresses belonging to the given address family which are assigned to the adapter with the given index.

## Return Values

The count of addresses of the given address family will be returned.

## Example

```c
on start
{
  const dword AF_INET = 2;   // IPv4 adapter family
  const dword AF_INET6 = 28; // IPv6 adapter family
  dword ifIdx;               // interface index
  long ipv4AdrCount;         // variable for count of all ipv4 addresses of first adapter
  long ipv6AdrCount;         // variable for count of all ipv6 addresses of first adapter

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    ipv4AdrCount = IpGetAdapterAddressCount( ifIdx, AF_INET );
    if (ipv4AdrCount != -1)
    {
      write("IpGetAdapterAddressCount: Adapter with index %d has %d IPv4 addresses assigned.", ifIdx, ipv4AdrCount);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterAddressCount: Error: The function call failed. Invalid ifIndex given for ipv4.");
    }

    ipv6AdrCount = IpGetAdapterAddressCount( ifIdx, AF_INET6 );
    if (ipv6AdrCount != -1)
    {
      write("IpGetAdapterAddressCount: Adapter with index %d has %d IPv6 addresses assigned.", ifIdx, ipv6AdrCount);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterAddressCount: Error: The function call failed. Invalid ifIndex given for ipv6.");
    }
  }
}
```

## Availability

| Since Version |
|---|
