# SomeIpGetValueDWord

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetValueDWord( dword objectHandle, char valuePath[] );
```

## Description

This function can be used to read out a raw value from the object specified in the objectHandle parameter. The value is accessed in this case via symbolic access paths.

## Return Values

Raw value
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
variables
{
  DWORD gPm; // provided method handle
}

void Initialize()
{
  DWORD aep; // application endpoint handle
  DWORD psi; // provided service instance handle

  // open application endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create service instance
  psi = SomeIpCreateProvidedServiceInstance(aep,11,1);

  // create method
  gPm = SomeIpAddMethod(psi,31,"OnMethodRequest");
}

void OnMethodRequest(dword methodHandle,dword messageHandle,dword messageResponseHandle)
{
  WORD val1; // value of input parameter 1
  WORD val2; // value of input parameter 2
  DWORD res; // value of return parameter

  // get value from request
  val1 = (WORD)SomeIpGetValueDWord(messageHandle,"Member_value1");
  val2 = (WORD)SomeIpGetValueDWord(messageHandle,"Member_value2");

  // calculate result
  res = val1 + val2;

  // set response value
  SomeIpSetValueDWord(messageResponseHandle,"Result",(val1 + val2));
}
```

## Availability

| Since Version |
|---|
