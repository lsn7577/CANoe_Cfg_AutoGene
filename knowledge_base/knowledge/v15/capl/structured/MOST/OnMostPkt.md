# OnMostPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostPkt(long pktdatalen);
```

## Description

When a packet is received over the Asynchronous Channel the OnMostPkt() event procedure is called.

The following functions are available for evaluating the event:

In nodal sequences (Measurement Setup) a received packet can be passed to the next node by the outputMostPktThis command.

## Parameters

| Name | Description |
|---|---|
| pktdatalen | Number of data bytes of the packet. |

## Return Values

—

## Example

Access to packet data:

```c
OnMostPkt(long pktDataLen)
{
   byte data[1524];
   long i, bytesdisp;
   write("Packet detected on channel %d", mostPktMsgChannel());
   // copy packet data to local buffer
   mostPktGetData(data, pktDataLen);
   // output first data bytes
   bytesdisp = pktDataLen > 10 ? 10 : pktDataLen;
   for(i = 0; i < bytesdisp; i++)
   {
      write("Byte %03d: %02X", i, data[i]);
   }
   // forward packet to the next node
   outputMostPktThis();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0: MOST25 7.1 SP2: MOST150 7.2 SP3: MOST50 | 5.0: MOST25 7.1 SP2: MOST150 7.2 SP3: MOST50 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
