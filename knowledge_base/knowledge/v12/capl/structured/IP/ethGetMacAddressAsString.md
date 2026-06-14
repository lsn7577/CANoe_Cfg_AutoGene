# ethGetMacAddressAsString

> Category: `IP` | Type: `function`

## Syntax

```c
long ethGetMacAddressAsString( qword macAddr, char buffer[], dword bufferLength );
```

## Description

Converts a MAC address from qword to string. The function is helpful with ethernetPacket.source and ethernetPacket.destination.

## Return Values

0: The function completed successfully.

## Example

```c
on ethernetPacket *
{
  char macAddrStr[18];
  if (ethGetMacAddressAsString( this.source, macAddrStr, elcount(macAddrStr) ) == 0)
  {
    write("Received Ethernet packet from %s", macAddrStr );
  }
}
```

## Availability

| Since Version |
|---|
