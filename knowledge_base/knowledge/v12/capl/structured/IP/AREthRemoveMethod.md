# AREthRemoveMethod

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthRemoveMethod( dword methodHandle );
```

## Description

This function removes a method from a Provided Service Instance.

Afterwards, the callback registered with AREthAddMethod is no longer called.

## Return Values

0: The function was successfully executed

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

on key 'r'
{
  // remove method
  AREthRemoveMethod(gPm);
}
```

## Availability

| Since Version |
|---|
