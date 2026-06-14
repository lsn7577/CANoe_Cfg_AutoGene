# TestGetWaitPDUsTPTCPSrcPort

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitPDUsTPTCPSrcPort(dword &tcpSourcePort); //form 1
long TestGetWaitPDUsTPTCPSrcPort(dword explicitJoinIndex, dword &tcpSourcePort); //form 2
```

## Description

If a PDU was received via TCP that triggered the last wait function, with form 1 the TCP source port can be requested.

Form 2 can only be used for joined events. The number of the joined event (return value of TestJoin...) is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| tcpSourcePort | TCP source port. |
| explicitJoinIndex | Number of the joined event corresponds with the return value of TestJoin.... |

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
      && TestGetWaitPDUsTPTCPSrcPort(srcPort)==0
      && TestGetWaitPDUsTPTCPDstPort(dstPort)==0)
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
