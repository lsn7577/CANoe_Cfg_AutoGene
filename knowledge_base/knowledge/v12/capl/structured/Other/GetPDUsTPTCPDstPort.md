# GetPDUsTPTCPDstPort

> Category: `Other` | Type: `function`

## Syntax

```c
long GetPDUsTPTCPDstPort(this, dword &tcpDestinationPort);
```

## Description

This function can only be used within a on PDU handler. If the PDU was received via TCP, with this function the TCP destination port can be requested.

## Return Values

0: Data access successful.

## Example

```c
on PDU engineDataPDU
{
  dword srcAddr, dstAddr, srcPort, dstPort;
  char srcAddrAsString[16], dstAddrAsString[16];

  if (GetPDUsTPIPv4SrcAddr(this, srcAddr)==0
    && GetPDUsTPIPv4DstAddr(this, dstAddr)==0)
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
