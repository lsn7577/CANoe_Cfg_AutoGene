# IpGetAdapterAddressAsString

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterAddressAsString( dword ifIndex, char address[], dword count);
```

## Description

The function retrieves the string representation of the first address associated with the specified network interface.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  const dword IPV4_STR_SIZE = 16; // IPv4 string size
  char ipAddr[IPV4_STR_SIZE];     // human readable ipv4 address string.
  dword ifIdx;                    // interface index
  long result;                    // function result.

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    result = IpGetAdapterAddressAsString( ifIdx, ipAddr, elcount(ipAddr) );
    if (result == 0)
    {
      // success.
      write("IpGetAdapterAddressAsString for adapter %d returned: %s", ifIdx, ipAddr);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterAddressAsString: Error %d", result);
      // handle error...
    }
  }
}
```

## Availability

| Since Version |
|---|
