# AREthGetValueString

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetValueString( dword objectHandle, char valuePath[], dword bufferLength, char buffer[] );
```

## Description

This function can be used to read out a string from the object specified in the objectHandle parameter.

For Enum data types, the function returns the symbolic value.

## Return Values

Number of copied bytes
In case of an error, the function returns 0, and the exact Error code can be queried with AREthGetLastError.
See BOM in SOME/IP UTF8 and UTF16 strings

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
  CHAR Member_value1[256];  // value of input parameter 1
  WORD val2;                // value of input parameter 2
  dword res;                // value of return parameter

  // get value from request
  AREthGetValueString(messageHandle,"Member_value1",elcount(Member_value1),Member_value1);
  val2 = (WORD)AREthGetValueDWord(messageHandle,"Member_value2");

  // do something here
}
```

## Availability

| Since Version |
|---|
