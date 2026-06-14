# diagGetParameterCoded, diagSetParameterCoded

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterCoded(diagResponse obj, char parameterName[], byte* buffer, dword bufferSize)
```

## Description

Sets or specifies the value of a parameter directly via coded data bytes.

## Return Values

0 if bytes were copied, otherwise <0 for an error code.

## Availability

| Since Version |
|---|
