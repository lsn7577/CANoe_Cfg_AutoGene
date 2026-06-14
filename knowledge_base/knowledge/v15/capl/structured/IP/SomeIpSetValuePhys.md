# SomeIpSetValuePhys

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetValuePhys( dword objectHandle, char valuePath[], float value);
```

## Description

This function can be used to set a physical value in the object specified in the objectHandle parameter.

All necessary information such as data type and conversion formula must be stored in the FIBEX database.

## Parameters

| Name | Description |
|---|---|
| objectHandle | Handle to a SOME/IP IL ObjectThe following objects are supported: Messages Fields Method calls: Handle to a method call that was created with SomeIpCreateMethodCall. |
| valuePath | Path of the value to be set.For specification of complex paths, a corresponding syntax must be adhered to (see also Syntax for Database-based Access Paths). |
| value | New physical value |

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters Member_value1 and Member_value2, and a return parameter Result. For the return parameter Result a factor and offset is set in the database.

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
  val1 = (WORD)SomeIpGetValueDword(messageHandle,"Member_value1");
  val2 = (WORD)SomeIpGetValueDword(messageHandle,"Member_value2");

  // calculate result
  res = val1 + val2;

  // set response value
  SomeIpSetValuePhys(messageResponseHandle,"Result",(val1 + val2));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
