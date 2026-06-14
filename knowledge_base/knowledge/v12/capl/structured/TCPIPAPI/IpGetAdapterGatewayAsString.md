# IpGetAdapterGatewayAsString

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterGatewayAsString( dword ifIndex, char address[], dword count);
```

## Description

The function retrieves the string representation of the default gateway address associated with the specified network interface.

Gateway information is not yet available before the start of the measurement (on pre-start). Rather it is first available at the start of the measurement (on start) as soon as the stack has been completely initialized.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  const dword IPV4_STR_SIZE = 16;    // IPv4 string size
  dword ifIdx;                       // interface index
  char ipv4GwAddrStr[IPV4_STR_SIZE]; // human readably IPv4 Gateway address.
  long result;                       // function result.

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    result = IpGetAdapterGatewayAsString( ifIdx, ipv4GwAddrStr, elcount(ipv4GwAddrStr) );
    if (result == 0)
    {
      // success.
      write("IpGetAdapterGatewayAsString for adapter %d returned IPv4 gateway address: %s", ifIdx, ipv4GwAddrStr);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterGatewayAsString: Error %d", result);
    }
  }
}
```

## Availability

| Since Version |
|---|
