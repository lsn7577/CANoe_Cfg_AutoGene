# AREthGetValueDWord

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetValueDWord( dword objectHandle, char valuePath[] );
```

## Description

This function can be used to read out a raw value from the object specified in the objectHandle parameter. The value is accessed in this case via symbolic access paths.

## Return Values

Raw value
In the Event of an error, the function returns the value 0. The AREthGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
variables
{
  dword gPm; // provided method handle
}

void Initialize()
{
  dword aep; // application endpoint handle
  dword psi; // provided service instance handle

  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create service instance
  psi = AREthCreateProvidedServiceInstance(aep,11,1);

  // create method
  gPm = AREthAddMethod(psi,31,"OnMethodRequest");
}

void OnMethodRequest(dword methodHandle,dword messageHandle,dword messageResponseHandle)
{
  WORD val1; // value of input parameter 1
  WORD val2; // value of input parameter 2
  dword res; // value of return parameter

  // get value from request
  val1 = (WORD)AREthGetValueDWord(messageHandle,"Member_value1");
  val2 = (WORD)AREthGetValueDWord(messageHandle,"Member_value2");

  // calculate result
  res = val1 + val2;

  // set response value
  AREthSetValueDWord(messageResponseHandle,"Result",(val1 + val2));
}
```

## Availability

| Since Version |
|---|
