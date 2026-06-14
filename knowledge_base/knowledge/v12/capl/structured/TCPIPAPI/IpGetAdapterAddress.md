# IpGetAdapterAddress

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterAddress( dword ifIndex, dword ipv4address[],dword ipv4AddressSize); // form 1
```

## Description

The function retrieves the addresses associated with a network interface. The interface is specified by it's 1-based index in the list of network interfaces, i.e. the first interface has index 1.

All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  IP_Address addresses[10];
  dword addressesCount;
  IP_Address addrMasks[10];
  dword addrMasksCount;
  long addrIdx;
  long ifIdx;

  write( "IP Configuration" );

  for( ifIdx = 1; ifIdx <= ipGetAdapterCount(); ifIdx++)
  {
    ipGetAdapterAddress( ifIdx, addresses, addressesCount );
    ipGetAdapterMask( ifIdx, addrMasks, addrMasksCount );
    for( addrIdx = 0; addrIdx < addressesCount; addrIdx++ )
    {
      char addrStr[30];
      char maskStr[30];
      addresses[addrIdx].PrintAddressToString( addrStr );
      addrMasks[addrIdx].PrintAddressToString( maskStr );

      write( "  %d. %s | %s", addrIdx+1, addrStr, maskStr );
    }
  }
}
```

## Availability

| Since Version |
|---|
