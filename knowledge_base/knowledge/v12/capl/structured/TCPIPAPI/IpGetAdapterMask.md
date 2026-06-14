# IpGetAdapterMask

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterMask( dword ifIndex, dword mask[], dword maskSize); // form 1
```

## Description

The function retrieves the address masks (subnet masks) associated with the specified network interface.

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
