# mostMHPConnectionSetTraceColors

> Category: `MOST` | Type: `function`

## Syntax

```c
mostMHPErrorSetTraceColors(long font, long bkgnd)
```

## Description

Sets the text and background color for displaying the MOST event in the Trace Window. The makeRGB function can be used for the colors.

## Return Values

0: OK

## Example

```c
OnMostMHPError (long sourceDevID, long destDevID, long fBlockID, long  instID, long functionID, long opType) 
{
   mostMHPErrorSetTraceColors(makeRGB(0, 0, 0), makeRGB(255, 0, 0)  );
   return 1; // Forward the MHPError-Event to the next node in the  Measurement Setup
}
```

## Availability

| Since Version |
|---|
