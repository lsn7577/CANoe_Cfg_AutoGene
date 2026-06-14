# GetEthernetPacket

> Category: `Other` | Type: `function`

## Syntax

```c
long GetEthernetPacket(this, ethernetPacket * packet);
```

## Description

This function can only be called inside of an on PDU handler. The function will return in its second parameter the Ethernet packet, the PDU was contained.

## Return Values

0: Data access successful.

## Example

```c
on PDU PDU_B
{
  ethernetPacket * aPacket_01;
  long result;
  result = GetEthernetPacket(this, aPacket_01); // PDU is assumed to be sent on ETH
  if (result == 0)
  {
    write("Received PDU 'PDU_B' in ETH packet with FCS %lu", aPacket_01.FCS);
  }
  else
  {
    write("Error accessing PDU!");
  }
}
```

## Availability

| Since Version |
|---|
