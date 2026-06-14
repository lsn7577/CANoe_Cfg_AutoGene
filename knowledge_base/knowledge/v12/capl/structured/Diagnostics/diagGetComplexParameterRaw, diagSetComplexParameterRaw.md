# diagGetComplexParameterRaw, diagSetComplexParameterRaw

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetComplexParameterRaw (diagResponse obj, char parameterName[], dword iteration, char subParameter[], BYTE* buffer, dword buffersize)
```

## Description

Reads/sets the complex parameter to the specified raw value.

## Return Values

Number of bytes copied into the buffer or error code.

## Availability

| Since Version |
|---|
