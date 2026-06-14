# TestGetWaitPDUsTPIPv4DstAddr

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitPDUsTPIPv4DstAddr(dword &IPv4DestinationAddress); //form 1
```

## Description

If a PDU was received via IPv4 that triggered the last wait function, with form 1 the IPv4 destination address can be requested.

Form 2 can only be used for joined events. The number of the joined event (return value of TestJoin...) is here being used as an index.

## Return Values

0: Data access successful.

## Example

```c
testcase TC_CheckPDUTPProperties()
{
  dword srcAddr, dstAddr, srcPort, dstPort;
  if (TestWaitForPDU(engineDataPDU, 0, 200)!=1)
  {
    TestStepFail("PDU not received");
  }
  else
  {
    if (TestGetWaitPDUsTPIPv4SrcAddr(srcAddr)==0
      && TestGetWaitPDUsTPIPv4DstAddr(dstAddr)==0
      && TestGetWaitPDUsTPUDPSrcPort(srcPort)==0
      && TestGetWaitPDUsTPUDPDstPort(dstPort)==0)
    {
      if (srcAddr != IpGetAddressAsNumber("192.168.0.1"))
        TestStepFail("source address not matching");
      else if (dstAddr != IpGetAddressAsNumber("192.168.0.2"))
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
