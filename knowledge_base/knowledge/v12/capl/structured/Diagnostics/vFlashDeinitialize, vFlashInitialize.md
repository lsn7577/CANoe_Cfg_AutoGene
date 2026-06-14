# vFlashDeinitialize, vFlashInitialize

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashInitialize();
```

## Description

Initializes (deinitializes) vFlash. Further API calls are only allowed after the CAPL callback vFlashInitializeCompleted (or vFlashDeinitializeCompleted) was called!

Note: This event-driven API is only needed outside of test modules or test units.

## Return Values

—

## Availability

| Since Version |
|---|
