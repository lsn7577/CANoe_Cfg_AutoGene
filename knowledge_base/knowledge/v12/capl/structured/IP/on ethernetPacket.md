# on ethernetPacket

> Category: `IP` | Type: `event`

## Syntax

```c
on ethernetPacket *;
```

## Description

The event procedure is called on the receipt of a valid Ethernet packet.

To access the control information you would use selectors.

The key word this is available within an on ethernetPacket procedure, to access the data of the packet that has just been received.

CAPL programs are by default not transparent to bus events. This means that a CAPL node in the evaluation branch of the measurement configuration will block the data flow to its right side. You must explicitly program the passing of messages in CAPL nodes in the evaluation branch.

To make the CAPL node transparent to messages you would write:

## Example

```c
on ethernetPacket msgChannel1.*
{
  write("Received Ethernet packet with length %d", this.Length );
  output( this ); // only required in CAPL node in measurement setup!
}
```

## Availability

| Since Version |
|---|
