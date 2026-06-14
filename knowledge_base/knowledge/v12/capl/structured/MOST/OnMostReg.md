# OnMostReg

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostReg()
```

## Description

OnMostReg() is called in response to read or write requests to registers of a MOST hardware interface chip.

The following functions are available for evaluating the event:

For further information on this event see Supplemental Information on Event Procedures for MOST Controller Events.

## Return Values

—

## Example

```c
OnMostReg()
{
  byte regData[16];
  long i, offset;
  // get register contents
  mostRegGetData(regData, 16);
  // get offset
  offset = mostRegOffset();
  // output register contents to Write Window
  write("OnMostReg() called for chip %d on channel %d", mostRegChip(), mostEventChannel());
  write("Map   Value");
  for(i = 0; i < mostRegDataLen(); i++)
  {
    write("%04X  %02X", offset + i, regData[i]);
  }
}

OnMostReg() called for chip 1 on channel 1
Map   Value
0080  E2
0081  42
0082  16
...
```

## Availability

| Since Version |
|---|
