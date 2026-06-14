# mostMHPPacketSetTraceColors

> Category: `MOST` | Type: `function`

## Syntax

```c
mostMHPPacketSetTraceColors(long font, long bkgnd)
```

## Description

Sets the text and background color for displaying the MOST event in the Trace Window. The makeRGB function can be used for the colors.

## Return Values

0: OK

## Example

```c
OnMostMHPPacket (long  sourceDevID, long destDevID, long fBlockID, long instID, long functionID, long  opType)
{
   mostMHPPacketSetTraceColors(makeRGB(0, 0, 0), makeRGB(255, 0, 0) );
   return 1; // Forward the MHPPacket to the next node in the Measurement Setup
}
```

## Availability

| Since Version |
|---|
