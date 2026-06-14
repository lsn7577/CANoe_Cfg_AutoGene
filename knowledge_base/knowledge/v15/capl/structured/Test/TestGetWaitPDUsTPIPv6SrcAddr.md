# TestGetWaitPDUsTPIPv6SrcAddr

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitPDUsTPIPv6SrcAddr(byte IPv6SourceAddress[]); //form 1
long TestGetWaitPDUsTPIPv6SrcAddr(dword explicitJoinIndex, byte IPv6SourceAddress[]); //form 2
```

## Description

If a PDU was received via IPv6 that triggered the last wait function, with form 1 the IPv64 source address can be requested.

Form 2 can only be used for joined events. The number of the joined event (return value of TestJoin...) is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| IPv6DestinationAddress | IPv6 source address as 16 byte array. |
| explicitJoinIndex | Number of the joined event corresponds with the return value of TestJoin.... |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
