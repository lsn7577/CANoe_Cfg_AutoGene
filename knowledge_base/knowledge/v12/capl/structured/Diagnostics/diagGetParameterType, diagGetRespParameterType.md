# diagGetParameterType, diagGetRespParameterType

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterType(diagResponse object, char[] qualifier, char[] buffer, DWORD bufferSize)
```

## Description

Retrieve the qualifier of the parameter's type.

## Return Values

Length of qualifier written to buffer, may be truncated.

## Availability

| Since Version |
|---|
