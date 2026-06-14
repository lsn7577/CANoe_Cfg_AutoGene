# diagGetRespParameterRaw

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetRespParameterRaw (diagRequest req, char parameterName[], byte buffer[], dword bufferLen);
```

## Description

This function offers access to parameters contained in a received response object, whereby the function is addressed directly by the request. This eliminates the need to generate a separate response object. If no response is available yet for the request, an error is reported.

## Return Values

0 if bytes were copied, otherwise <0 for an error code

## Availability

| Since Version |
|---|
