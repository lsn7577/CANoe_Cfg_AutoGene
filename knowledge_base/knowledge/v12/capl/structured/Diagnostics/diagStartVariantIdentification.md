# diagStartVariantIdentification

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagStartVariantIdentification();
```

## Description

Start the automatic variant identification algorithm for the given target, or the currently selected one if none is given. The algorithm will communicate via the built-in diagnostic channel, i.e. the CAPL callback functions are not used for the identification.

A tester module may wait for the completion of the algorithm with testWaitForDiagVariantIdentificationCompleted, or query the status of the identification with diagGetIdentifiedVariant.

## Return Values

0: No error, algorithm was started

## Availability

| Since Version |
|---|
