# GetPDUsTPIPv6SrcAddr

> Category: `Other` | Type: `function`

## Syntax

```c
long GetPDUsTPIPv6SrcAddr(this, byte IPv6SourceAddress[]);
```

## Description

This function can only be used within a on PDU handler. If the PDU was received via IPv6, with this function the IPv6 source address can be requested.

## Return Values

0: Data access successful.

## Example

```c
on PDU engineDataPDU
{
  dword srcPort, dstPort;
  byte srcAddr[16], dstAddr[16];
  char srcAddrAsString[40], dstAddrAsString[40];

  if (GetPDUsTPIPv6SrcAddr(this, srcAddr)==0
    && GetPDUsTPIPv6DstAddr(this, dstAddr)==0)
  {
    IpGetAddressAsString(srcAddr, srcAddrAsString, elcount(srcAddrAsString));
    IpGetAddressAsString(dstAddr, dstAddrAsString, elcount(dstAddrAsString));

    if(GetPDUsTPUDPSrcPort(this, srcPort)==0
      && GetPDUsTPUDPDstPort(this, dstPort)==0)
    {
      write("PDU received by UDP from %s:%u to %s:%u", srcAddrAsString, srcPort, dstAddrAsString, dstPort);
    }

    if (GetPDUsTPTCPSrcPort(this, srcPort)==0
      && GetPDUsTPTCPDstPort(this, dstPort)==0)
    {
      write("PDU received by TCP from %s:%u to %s:%u", srcAddrAsString, srcPort, dstAddrAsString, dstPort);
    }
  }
}
```

## Availability

| Since Version |
|---|
