# TestWaitForDiagVariantIdentificationCompleted, TestWaitForDiagEcuVariantIdentificationCompleted

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagVariantIdentificationCompleted(); // form 1
```

## Description

Waits for the completion of the automatic variant identification algorithm. If the qualifier of an expected variant is given, an error is returned if a different variant is identified.

## Return Values

1: Identification algorithm finished successfully

## Availability

| Since Version |
|---|
