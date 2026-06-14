# <OnAREthMethodRequest>

> Category: `IP` | Type: `function`

## Syntax

```c
void <OnAREthMethodRequest>( dword methodHandle, dword messageHandle, dword messageResponseHandle ); // form 1
```

## Description

A callback function with this signature must be passed to the CAPL function AREthAddMethod.

The syntax of the callback function specified in form 2 must be used if the fireAndForget parameter was used when the method was created by the provider (see also AREthAddMethod).

This callback is called when a consumer has called the method created with AREthAddMethod.

## Return Values

—

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters (Member_value1 and Member_value2), and a return parameter (Result).

```c
variables
{
  dword gPm; // provided method handle
}

void Initialize()
{
  dword aep; // application endpoint handle
  dword psi; // provided Service Instance handle

  // open application endpoint
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
