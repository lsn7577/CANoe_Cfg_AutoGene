# TestGetWaitPDUsTPIPv6DstAddr

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitPDUsTPIPv6DstAddr(byte IPv6DestinationAddress[]); //form 1
```

## Description

If a PDU was received via IPv6 that triggered the last wait function, with form 1 the IPv6 destination address can be requested.

Form 2 can only be used for joined events. The number of the joined event (return value of TestJoin...) is here being used as an index.

## Return Values

0: Data access successful.

## Example

```c
long IPv6AddressEquals(byte addr1[], byte addr2[])
{
  int i;
  if (elcount(addr1)<16 || elcount(addr2)<16)
    return 0;

  for (i=0; i< 16; ++i)
    if (addr1[i]!=addr2[i])
      return 0;

    return 1;
}

testcase TC_CheckPDUTPProperties()
{
  dword srcPort, dstPort;
  byte  srcAddr[16], dstAddr[16], expectedSrcAddr[16], expectedDstAddr[16];
  if (TestWaitForPDU(engineDataPDU, 0, 200)!=1)
  {
    TestStepFail("PDU not received");
  }
  else
  {
    if (TestGetWaitPDUsTPIPv6SrcAddr(srcAddr)==0
      && TestGetWaitPDUsTPIPv6DstAddr(dstAddr)==0
      && TestGetWaitPDUsTPUDPSrcPort(srcPort)==0
      && TestGetWaitPDUsTPUDPDstPort(dstPort)==0)
    {
      IpGetAddressAsArray("2001::1", expectedSrcAddr);
      IpGetAddressAsArray("2001::2", expectedDstAddr);

      if (IPv6AddressEquals(srcAddr, expectedSrcAddr)!=1)
        TestStepFail("source address not matching");
      else if (IPv6AddressEquals(dstAddr, expectedDstAddr)!=1)
        TestStepFail("destination address not matching");
      else if (srcPort != 1234)
        TestStepFail("source port not matching");
      else if (dstPort != 4321)
        TestStepFail("destination port not matching");
    }
    else
      TestStepFail("could not retrieve expected PDU TP properties");
  }
}
```

## Availability

| Since Version |
|---|
