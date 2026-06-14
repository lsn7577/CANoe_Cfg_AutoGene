# diagIsRespParameterDefault

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsRespParameterDefault (diagRequest obj, char parameterName[])
```

## Description

Access/check a response parameter for a given request. It is not necessary to declare the response and retrieve the response explicitly e.g. via diagGetLastReponse(diagRequest) to make a check with diagResponse.IsParameterDefault("MyParamName").

Returns <> 0 if the parameter in the response has its default value.

## Return Values

Error code

## Example

```c
testfunction MainTest()
{
   diagRequest DefaultSession_Start req;
   diagSetTarget("Door");
   diagSendRequest(req);
   testWaitForDiagResponse(req, 2000);
   write("IsDefault(P3) = %d", diagIsRespParameterDefault(req, "P3"));
}
```

## Availability

| Since Version |
|---|
