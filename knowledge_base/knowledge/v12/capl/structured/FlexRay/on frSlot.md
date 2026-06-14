# on frSlot

> Category: `FlexRay` | Type: `event`

## Syntax

```c
on frSlot *
```

## Description

This event procedure is called up in each cycle after the slot is past. The event procedure is only called for slots in the static segment.

The event procedure is also called up if no frame is received in the specified slot.

Thus it will synchronously be executed to the FlexRay cycle. Therefore it cannot be used in the Measurement Setup or the analysis branch.

If any frame is not received in the slot, then the event procedure is called with the next slot that contains a frame or at the latest when the next cycle begins. For the VN interfaces it will be called approx. 500 microseconds after the slot.

If two frames are received in slot <slot ID> (on channel A and B), then the event procedure is called up just once (and in fact, with the frame contents of channel A).

The selectors always reference the contents of the Slot. The FrameType selector should be evaluated before further processing.

Value range for n: 1 <= <slot ID> <= max. static slot ID of the cluster configuration.

An optional channel parameter for event filtering can be assigned to all functions.

In the example, the event procedure is only called for frames whose FlexRay channel 2 ID is 35.

The following syntax is only possible with databases that do not contain PDUs:

## Example

The following program executes an action always when the static slot 60 is expired.

```c
on frSlot 60
{
   // 
 slot 60 is over ... do action ...
   // Note: The handler is called even if any frame
   // is not received in this slot!
   if (this.Type == 1) // valid Frame was received in this slot
   {

      // Attention: Frame can be from channel A or B.
      // If received on both, then only frame from channel A
      // 
 will be signaled and retrieved here.
   }
}
```

## Availability

| Since Version |
|---|
