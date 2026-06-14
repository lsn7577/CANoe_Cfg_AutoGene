# IpGetAdapterDescription

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterDescription( dword ifIndex, char name[], dword count);
```

## Description

The function retrieves the description of the specified network interface.

All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  const dword STR_SIZE = 256; // string buffer size
  char ifDescr[STR_SIZE];     // Interface description string.
  dword ifIdx;                // interface index
  long result;                // function result.

  for (ifIdx = 1; ifIdx <= IpGetAdapterCount(); ifIdx++)
  {
    result = IpGetAdapterDescription( ifIdx, ifDescr, elcount(ifDescr) );
    if (result == 0)
    {
      // success.
      write("IpGetAdapterDescription for adapter %d returned: %s", ifIdx, ifDescr);
    }
    else
    {
      writeLineEx(1, 3, "IpGetAdapterDescription: Error %d", result);
    }
  }
}
```

## Availability

| Since Version |
|---|
