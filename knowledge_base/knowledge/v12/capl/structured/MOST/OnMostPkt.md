# OnMostPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostPkt(long pktdatalen)
```

## Description

When a packet is received over the Asynchronous Channel the OnMostPkt() event procedure is called.

The following functions are available for evaluating the event:

In nodal sequences (Measurement Setup) a received packet can be passed to the next node by the outputMostPktThis command.

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

| Since Version |
|---|
