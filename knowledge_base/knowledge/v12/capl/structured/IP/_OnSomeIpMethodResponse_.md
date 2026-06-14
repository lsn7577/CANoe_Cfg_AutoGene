# <OnSomeIpMethodResponse>

> Category: `IP` | Type: `function`

## Syntax

```c
void <OnSomeIpMethodResponse>(dword methodCallHandle, dword messageResponseHandle );
```

## Description

A callback function with this signature must be passed to the CAPL function SomeIpCreateMethodCall.

## Return Values

—

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters (Member_value1 and Member_value2), and a return parameter (Result).

```c
variables
{
  DWORD gMc; // global method call handle
}

void Initialize()
{
  DWORD aep; // application endpoint handle
  DWORD csi; // consumed Service Instance handle

  // open application endpoint
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
