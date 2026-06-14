# mostEthPktSetTraceColors

> Category: `MOST` | Type: `function`

## Syntax

```c
mostEthPktSetTraceColors(long font, long bkgnd)
```

## Description

Sets the text and background color for displaying the MOST event in the Trace Window. The makeRGB function can be used for the colors.

## Return Values

0: OK

## Example

```c
OnMostEthPkt
{
   mostEthPktSetTraceColors(makeRGB(0, 0, 0), makeRGB(255, 0, 0) );
   outputMostEthPktThis(); // Forwards this packet to the node in the Measurement Setup
}
```

## Availability

| Since Version |
|---|
