# mostPktSetTraceColors

> Category: `MOST` | Type: `function`

## Syntax

```c
mostPktSetTraceColors(long font, long bkgnd)
```

## Description

Sets the text and background color for displaying the MOST event in the Trace Window. The makeRGB function can be used for the colors.

## Return Values

0: OK

## Example

```c
OnMostPkt (long  pktlen) 
{
   mostPktSetTraceColors(makeRGB(0, 0, 0), makeRGB(255,  0, 0) );   
   outputMostPktThis(); // Forwards this packet to the node in the  Measurement Setup 
}
```

## Availability

| Since Version |
|---|
