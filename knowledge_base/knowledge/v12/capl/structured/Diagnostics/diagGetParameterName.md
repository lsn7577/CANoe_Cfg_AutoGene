# diagGetParameterName

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterName (diagResponse obj, dword paramNo, char buffer[], dword buffersize)
```

## Description

Writes the qualifier (without parent path) of the diagnostic parameter into the given field. Structural parameters are counted too.

## Return Values

Number of chars written to buffer or error code.

## Availability

| Since Version |
|---|
