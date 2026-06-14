# FlexRayRcvStatusEvent

> Category: `FlexRay` | Type: `function`

## Syntax

```c
FlexRayRcvStatusEvent (long msgTime, int channel, long statusType, long infomask1, long infomask2, long infomask3);
```

## Description

This function is a callback and is called by the tool!

The callback occurs when the FlexRay Communication Controller (CC) has synchronized with the bus or the synchronization fails.

## Return Values

—

## Example

```c
variables
{
   int busIsSynchronized = 0;
}
FlexRayRcvStatusEvent (long msgTime, int channel, long statusType, long infomask1, long infomask2, long infomask3)
{
   if (statusType & 0x00000001)
   {
      if (infomask1 & 0x00000001)
      {
         busIsSynchronized = 1;
         Write("FR StatusEvent: Bus (channel %d) is synchronized.", channel);
      }
      else
      {
         Write("FR StatusEvent: Bus (channel %d) lost synchronization.", channel);
         if (busIsSynchronized == 1) ResetFlexRayCC(channel);
         busIsSynchronized = 0;
      }
    }
}
```

## Availability

| Since Version |
|---|
