# frGetFrameCRC

> Category: `FlexRay` | Type: `function`

## Syntax

```c
dword frGetFrameCRC(this);
```

## Description

This function returns the CRC of a received FlexRay frame.

The Header CRC can be determined with a special selector of the event procedure.

## Return Values

Frame CRC (data type WORD).
The return value is only valid if the frame was received by a Vector FlexRay hardware interface in asynchronous monitor mode. In any other case 0 will be sent back.

## Example

The following example writes the CRC into the Write Window for all received frames.

```c
on frFrame *
{
   dword 
 crc;
   crc 
 = frGetFrameCRC(this);
   Write(“Frame %d in Cycle %d has CRC 0x%x”, this.FR_SlotID, this.FR_Cycle, crc);
   output(this); // only required in Measurement Setup
}
```

## Availability

| Since Version |
|---|
