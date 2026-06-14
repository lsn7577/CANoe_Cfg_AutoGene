# testWaitForScopeAnalyseBitSegments

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeAnalyseBitSegments(message aMessage, ScopeAnalyseBitSegment bitSegments[], dword noOfSegments, dword referenceVoltagePoint, dword flags, dword msgFieldStart, dword msgFieldEnd);
```

## Description

Starts an analysis for the defined bit segments for each bit, which is within the defined range. The result of the analysis can be requested with the function testWaitScopeGetAnalysedBitSegments.

## Availability

| Since Version |
|---|
