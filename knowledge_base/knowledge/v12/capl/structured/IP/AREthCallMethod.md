# AREthCallMethod

> Category: `IP` | Type: `function`

## Syntax

```c
LONG AREthCallMethod( dword methodHandle );
```

## Description

Initiates a method call by sending a request to the server.

The service that the method contains must be offered by the provider through an Offer Service message and still be valid so that the method can be successfully called.

Background:

For a successful method call, the remote address and the remote port of the provided service is needed. This is communicated via the Offer Service message.

## Return Values

0: The function was successfully executed

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters Member_value1 and Member_value2, and a return parameter Result.

```c
variables
{
  dword gMc; // global method call handle
}

void Initialize()
{
  dword aep; // application endpoint handle
  dword csi; // consumed Service Instance handle

  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(0x11, 50002);

  // cretae Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,11,1);

  // create method call
  gMc = AREthCreateMethodCall(csi,31,"OnMethodResponse");
}

on key 's'
{
  // if this key is pressed the method should be called

  // set the two input parameters of the method
  AREthSetValueDWord(gMc,"Member_value1",11);
  AREthSetValueDWord(gMc,"Member_value2",22);

  // call the method
  AREthCallMethod(gMc);
}

void OnMethodResponse(dword methodCallHandle, dword messageResponseHandle )
{
  dword res; // value of return parameter

  // get the returned parameter values
  res = AREthGetValueDWord(messageResponseHandle,"Result");

  write("The method call returned value: %d",res);
}
```

## Availability

| Since Version |
|---|
