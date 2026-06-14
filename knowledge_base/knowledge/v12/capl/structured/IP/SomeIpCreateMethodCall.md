# SomeIpCreateMethodCall

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpCreateMethodCall( dword csiHandle, dword methodId, char onSomeIpMethodResponse [] ); // form 1
```

## Description

This function creates a method call for the consumer. By means of the return value of the function, the method parameters can be set using SomeIpSetValue.... The method is then called using SomeIpCallMethod.

If the function is called with the syntax specified in form 1, the method call takes place asynchronously. At the same time, the client is not blocked after the method call until the corresponding response. A synchronous method call is not supported by SOME/IP IL.

The syntax specified in form 2 must be used if the fireAndForget parameter was used when the method was created for the provider (see also SomeIpAddMethod).

The method call can be removed again using the SomeIpRemoveMethodCall function.

## Return Values

0: An error occurred. The error can be evaluated using the SomeIpGetLastError function.

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters Member_value1 and Member_value2, and a return parameter Result.

```c
variables
{
  DWORD gMc; // global method call handle
}

void Initialize()
{
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle

  // open Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(0x11, 50002);

  // cretae Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,11,1);

  // create method call
  gMc = SomeIpCreateMethodCall(csi,31,"OnMethodResponse");
}

on key 's'
{
  // if this key is pressed the method should be called

  // set the two input parameters of the method
  SomeIpSetValueDWord(gMc,"Member_value1",11);
  SomeIpSetValueDWord(gMc,"Member_value2",22);

  // call the method
  SomeIpCallMethod(gMc);
}

void OnMethodResponse(dword methodCallHandle, dword messageResponseHandle )
{
  DWORD res; // value of return parameter

  // get the returned parameter values
  res = SomeIpGetValueDWord(messageResponseHandle,"Result");

  write("The method call returned value: %d",res);
}
```

## Availability

| Since Version |
|---|
