# SOMEIP_InjectPDU

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SOMEIP_InjectPDU(PDU pdu, long channel, IP_Endpoint srcIPEndpoint, IP_Endpoint dstIPEndpoint);
```

## Description

Injects the PDU into the SOME/IP-Binding block, where its then send.

## Parameters

| Name | Description |
|---|---|
| pdu | PDU which should be injected. |
| channel | Channel of the network where the PDU should be injected. |
| srcIPEndpoint | IP endpoint of the PDU sender. |
| dstIPEndpoint | IP endpoint of the PDU receiver. |

## Example

```c
on pdu *
{
  ip_endpoint srcEp, dstEp;
  ethernetPacket ethPkt;

  if (this.msgChannel == 2 && this.LongHeaderID!=0xFFFF8100)
  {
    GetEthernetPacket(this, ethPkt);
    if (ethPkt.hwPort == ethernetPort::Ethernet2::ReplayBlock_1)
    {
      GetPDUsTPSrcIPEndpoint(this, srcEp);
      GetPDUsTPDstIPEndpoint(this, dstEp);
      SOMEIP_InjectPDU(this, 1, srcEp, dstEp);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 SP2 | — | — | — | 6 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
