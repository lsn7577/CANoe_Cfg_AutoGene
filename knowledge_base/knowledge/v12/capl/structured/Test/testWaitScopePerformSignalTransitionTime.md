# testWaitScopePerformSignalTransitionTime

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopePerformSignalTransitionTime (message aMessage, ScopeAnalyseRange range, dword flags, long thresholdStart, long thresholdEnd, ScopeBitTransitionTimeResult result, ScopeAnalyseHandle handle); // form 1
```

## Description

Form 1: Measures the transition time of rising and falling edges of a CAN message within the defined area.

Form 2: Measures the transition time of rising and falling edges of all Tx messages of an ECU node within the defined area.

Form 3: Measures the transition time of rising and falling edges of a LIN message within the defined area.

Form 4: Measures the transition time of rising and falling edges of a FlexRay message within the defined area.

## Return Values

1 = success

## Availability

| Since Version |
|---|
