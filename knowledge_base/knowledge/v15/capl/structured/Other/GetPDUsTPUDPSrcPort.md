# GetPDUsTPUDPSrcPort

> Category: `Other` | Type: `function`

## Syntax

```c
long GetPDUsTPUDPSrcPort(this, dword &udpSourcePort);
```

## Description

This function can only be used within a on PDU handler. If the PDU was received via UDP, with this function the UDP source port can be requested.

## Parameters

| Name | Description |
|---|---|
| this | Handle to the currently handled (received) PDU object. |
| udpSourcePort | UDP source port. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP3 | 9.0 SP3 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
