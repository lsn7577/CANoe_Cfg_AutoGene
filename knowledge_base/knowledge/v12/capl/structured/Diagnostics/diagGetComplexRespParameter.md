# diagGetComplexRespParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetComplexRespParameter (diagRequest req, char parameterName[], dword iteration, char subParameter[], double output[]);
```

## Description

Returns the value of a numeric complex parameter.

This function offers access to parameters contained in a received response object, whereby the function is addressed directly by the request. This eliminates the need to generate a separate response object. If no response is available yet for the request, an error is reported.

## Return Values

Error code,
or value of the parameter or 0.0 if this could not be acquired.

## Availability

| Since Version |
|---|
