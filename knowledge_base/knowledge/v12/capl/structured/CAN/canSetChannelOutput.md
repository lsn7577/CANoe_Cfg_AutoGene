# canSetChannelOutput

> Category: `CAN` | Type: `function`

## Syntax

```c
long canSetChannelOutput(long channel, long silent);
```

## Description

Defines the response of the CAN controller to the bus traffic and sets the ACK bit.The CAN transmitter of the channel is switched off. So CANoe does not generate an Ack bit here, and messages can no longer be sent. It is still possible to receive messages.

## Return Values

0: ok

## Example

```c
on key 's'
{
   long channel =2;
      long silent =0;
   canSetChannelOutput(channel,silent);
   Write("silent set to %d",silent);
}
```

## Availability

| Since Version |
|---|
