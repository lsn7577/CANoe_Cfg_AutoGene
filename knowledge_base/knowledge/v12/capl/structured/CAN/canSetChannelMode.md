# canSetChannelMode

> Category: `CAN` | Type: `function`

## Syntax

```c
long canSetChannelMode(long channel, long gtx, long gtxreq);
```

## Description

Activates/deactivates the TXRQ and Tx of the CAN controller. This function does nothing with the Ack bit.

## Return Values

0: ok

## Example

```c
on key 't'
{
   long channel =2;
   char gtx =1;
   char gtxreq =1;
   canSetChannelMode(channel,gtx,gtxreq);
   Write("Mode set to tx=%d, txreq=%d",gtx,gtxreq);
}
```

## Availability

| Since Version |
|---|
