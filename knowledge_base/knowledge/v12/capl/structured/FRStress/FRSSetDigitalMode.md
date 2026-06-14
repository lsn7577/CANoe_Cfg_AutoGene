# FRSSetDigitalMode

> Category: `FRStress` | Type: `function`

## Syntax

```c
long FRSSetDigitalMode (float baudrate, int channel, int payloadLength, double macrotickLengthUs, int TSSLengthBit, int cycleLengthUs, int numberStaticSlots, int actionPointOffsetMT, int staticSlotLengthMT, int TSSExtension)
```

## Description

Activates the digital disturbance mode of FRstress.Configuration functions that belong to another operating mode are ignored.

There are dependencies between the parameters according to the FlexRay specification.

## Return Values

0: successful

## Availability

| Since Version |
|---|
