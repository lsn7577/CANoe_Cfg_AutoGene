# diagGetIdentifiedVariant

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetIdentifiedVariant(char identifiedVariantOut[], dword bufferLen);
```

## Description

Retrieve the qualifier of the variant that has been identified by the last successful run of the automatic variant identification algorithm for given target, or the current target if no target is given. The function can also be used to determine whether the algorithm has finished.

## Return Values

>=0: Number of characters written into the buffer

## Availability

| Since Version |
|---|
