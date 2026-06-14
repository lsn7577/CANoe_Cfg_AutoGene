# diagGetParameterPath, diagGetRespParameterPath

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterPath( diagResponse object, dword paramNo, char[] buffer, dword bufferSize)
```

## Description

Returns the full qualifier path of the parameter at the given position in the primitive. Only leaf parameters that have a simple value are counted, i.e. structural parameters like container lists are NOT returned.

## Return Values

Length of path written to buffer, may be truncated.

## Availability

| Since Version |
|---|
