# frSetKeySlot

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetKeySlot (long channel, long channelMask, long keySlotIndex, long keySlotId, long keySlotUsage)
```

## Description

Configures one of two possible key slots that are to be sent for a FlexRay bus.

The change will be applied with the next reset of the interface hardware (e.g. by resetFlexRayCC or resetFlexRayCCEx).

## Return Values

—

## Availability

| Since Version |
|---|
