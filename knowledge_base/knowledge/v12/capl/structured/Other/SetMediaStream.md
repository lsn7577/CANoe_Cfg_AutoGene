# SetMediaStream

> Category: `Other` | Type: `function`

## Syntax

```c
SetMediaStream(panel, control, busType, channel, streamIndex, streamId[]);
```

## Description

Replaces the media stream at the specified index of the Panel Designer Media Stream Control during runtime.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

Setting media stream from Ethernet channel 1.

```c
on key 'x'
{
  byte streamId[8] = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x00, 0x01 };
  SetMediaStream("AVTP Video H.264", "Media Stream Control", eEthernet, 1, 0, streamId);
}
```

## Availability

| Since Version |
|---|
