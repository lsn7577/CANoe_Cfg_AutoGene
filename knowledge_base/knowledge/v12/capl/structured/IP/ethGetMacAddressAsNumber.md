# ethGetMacAddressAsNumber

> Category: `IP` | Type: `function`

## Syntax

```c
qword ethGetMacAddressAsNumber( char macAddrStr[] );
```

## Description

Converts a MAC address string, i.e. "02:00:00:00:00:01", to a qword-number, which can be used with ethernetPacket.source and ethernetPacket.destination.

## Return Values

The MAC address as qword or 0, if failed

## Example

```c
on key '1'
{
  ethernetPacket txPacket;
  txPacket.msgChannel = 1;
  txPacket.source      = ethGetMacAddressAsNumber( "20:00:00:00:00:01" );
  txPacket.destination = ethGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
  txPacket.Length      = 100;
  txPacket.type        = 0xF123;
  output( txPacket );
}
```

## Availability

| Since Version |
|---|
