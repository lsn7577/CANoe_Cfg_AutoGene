# SomeIpGetValuePhys

> Category: `IP` | Type: `function`

## Syntax

```c
float SomeIpGetValuePhys( dword objectHandle, char valuePath[] );
```

## Description

This function can be used to read out a physical value from the object specified in the objectHandle parameter.

All necessary information such as data type and conversion formula must be stored in the FIBEX database.

For large numerical values, conversion from real numbers to integers can result in deviations.

## Return Values

Physical value
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters Member_value1 and Member_value2, and a return parameter Result. For the variables Member_value1 and Member_value2 a factor and offset is set in the database.

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
  val1 = (WORD)SomeIpGetValuePhys(messageHandle,"Member_value1");
  val2 = (WORD)SomeIpGetValuePhys(messageHandle,"Member_value2");

  // calculate result
  res = val1 + val2;

  // set response value
  SomeIpSetValueDWord(messageResponseHandle,"Result",(val1 + val2));
}
```

## Availability

| Since Version |
|---|
