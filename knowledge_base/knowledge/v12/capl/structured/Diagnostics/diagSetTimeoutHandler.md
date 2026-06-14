# diagSetTimeoutHandler

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetTimeoutHandler (diagRequest obj, char callbackName[])
```

## Description

Sets the timeout callback for a request, or default timeout callback function. This function will be called if no response arrives at the tester within the timeout specified with diagSetTimeout.

## Return Values

Error code

## Example

```c
on start
{
  diagSetTimeoutHandler("Request_Timeout");
}

on key '1'
{
  DiagRequest SimECU.ReadDataByIdentifier_Process req;
  diagSendRequest(req);
}

void Request_Timeout()
{
  write("No response received within expected time frame!");
}
```

## Availability

| Since Version |
|---|
