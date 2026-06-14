# diagGetConfiguredVariant

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetConfiguredVariant(char configuredVariantOut[], DWORD bufferLen);
```

## Description

Retrieves the qualifier of the variant that is configured for the current target.

Retrieve the qualifier of the variant that is configured for the current or given target in the Diagnostics configuration dialog. It is possible to provide this qualifier to the automatic variant identification algorithm.

## Return Values

Length of qualifier written to buffer, may be truncated.
0: No error, OK
<0: Error code
Especially:-94: No target was selected

## Availability

| Since Version |
|---|
