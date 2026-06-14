# diagGetRespParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetRespParameter (diagRequest req, char parameterName[], double output[]);
```

## Description

Returns the value of the numeric parameter, either in an output field or as return value (without the possibility of checking the correct function).

This function offers access to parameters contained in a received response object, whereby the function is addressed directly by the request. This eliminates the need to generate a separate response object. If no response is available yet for the request, an error is reported.

## Return Values

Error code or value of the parameter.

## Availability

| Since Version |
|---|
