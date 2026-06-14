# diagGetComplexRespParameterRaw

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetComplexRespParameterRaw (diagRequest req, char parameterName[], dword iteration, char subParameter[], byte buffer[], dword bufferLen);
```

## Description

Reads/sets the complex parameter to the specified raw value.

This function offers access to parameters contained in a received response object, whereby the function is addressed directly by the request. This eliminates the need to generate a separate response object. If no response is available yet for the request, an error is reported.

## Return Values

Error code

## Availability

| Since Version |
|---|
