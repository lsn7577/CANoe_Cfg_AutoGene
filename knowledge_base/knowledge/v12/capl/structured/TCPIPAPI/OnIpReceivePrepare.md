# OnIpReceivePrepare

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long OnIpReceivePrepare(ethernetPacket * packet);
```

## Description

If the CAPL program implements this callback it is called right before a received packet will be dispatched to the TCP/IP stack.

It is possible to manipulate the content of the packet or to block the receiving of the package from the bus.

The callback is only available for simulation nodes using the individual TCP/IP stack instance. Check this setting in the TCP/IP Stack configuration dialog.

## Return Values

0: Block the Ethernet packet.

## Example

```c
long OnIpReceivePrepare(ethernetPacket * packet)
{
  // block all packets with a broadcast destination MAC id
  if(packet.destination == 0xFFFFFFFFFFFFLL)
  {
    write("packet blocked");
    return 0;
  }
  write("packet passed to tcp/ip stack");
  return 1;
}
```

## Availability

| Since Version |
|---|
