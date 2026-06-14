# testWaitScopeAnalyseSignal

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeAnalyseSignal (message aMessage, dword flags, dword msgFieldStart, dword msgFieldEnd, ScopeBitMaskPolygon bitMaskPolygon, long domVoltageThreshold , long recVoltageThreshold, ScopeAnalyseHandle handle); // form 1
```

## Description

Form 1: Checks the bits of a CAN message against the defined bit mask.

Form 2: Checks the bits of FlexRay frames which are transmitted by one node against the defined bit mask.

## Return Values

Form 1:

## Availability

| Since Version |
|---|
