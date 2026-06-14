# AREthAddMethod

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthAddMethod( dword psiHandle, dword methodId, char onMethodRequestCallback[] ); // form 1
```

## Description

This function adds a method to a Provided Service Instance that was created with AREthCreateProvidedServiceInstance.

If this method is called by a client through a SOME/IP request, the specified CAPL callback function is called. Only one CAPL callback function can be registered for each method.

If the function is added with the syntax specified in form 1, the method call by the client takes place asynchronously. At the same time, the calling client is not blocked after the method call until the corresponding response. A synchronous method call is not supported by AUTOSAR Eth IL.

A method can be removed again using the AREthRemoveMethod function.

## Return Values

0: An error occurred. The error can be evaluated using the AREthGetLastError function.

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters Member_value1 and Member_value2, and a return parameter Result.

```c
variables
{
  dword gPm; // provided method handle
}

void Initialize()
{
  dword aep; // Application Endpoint handle
  dword psi; // provided Service Instance handle

  // open Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
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
