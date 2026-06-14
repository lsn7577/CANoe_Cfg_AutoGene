# linConfigureResponseRange

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linConfigureResponseRange(byte[] frameIds, byte[] dlcs, byte[][8] responseData)
```

## Description

Configures a range of frames as response of a LIN node if no database is used.

This function may only be called in the event procedure on preStart.

All of the array parameters must contain the same number of elements.

## Return Values

Returns 1 if the configuration of all given frames succeeded, otherwise 0.

## Example

```c
// Configure two LIN frames with the IDs 0x01 and 0x02 as response of the slave. The first frame contains 5 and the second one 2 data bytes.

on preStart
{
  byte ids[2] = { 0x01, 0x02 };
  byte dlcs[2] = { 5, 2 };
  byte responseData[2][8];

  responseData[0][0] =  0x55;
  responseData[0][1] =  0x55;
  responseData[0][2] =  0x55;
  responseData[0][3] =  0x55;
  responseData[0][4] =  0x55;

  responseData[1][0] =  0xAA;
  responseData[1][1] =  0xAA;

  linConfigureResponseRange(ids, dlcs, responseData);
}
```

## Availability

| Since Version |
|---|
