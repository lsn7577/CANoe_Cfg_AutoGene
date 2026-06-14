# IpGetAdapterMaskAsString

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterMaskAsString( dword ifIndex, char mask[], dword count);
```

## Description

The function retrieves the string representation of the first address mask associated with the specified network interface.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  const dword IPV4_STR_SIZE = 16;  // IPv4 string size
  dword ifIdx;                     // interface index
  long result;                     // function result.
  char ipv4AdrStr[IPV4_STR_SIZE];  // human readable IPv4 address string
  char ipv4MaskStr[IPV4_STR_SIZE]; // human readable IPv4 address mask string

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    IpGetAdapterAddressAsString( ifIdx, ipv4AdrStr, elcount(ipv4AdrStr) );
    result = IpGetAdapterMaskAsString( ifIdx, ipv4MaskStr, elcount(ipv4MaskStr) );
    if (result == 0)
    {
      // success.
      write("IpGetAdapterMask first IP %s of adapter with index %d has mask %s", ipv4AdrStr, ifIdx, ipv4MaskStr);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterMask: Error %d", result);
    }
  }
}
```

## Availability

| Since Version |
|---|
