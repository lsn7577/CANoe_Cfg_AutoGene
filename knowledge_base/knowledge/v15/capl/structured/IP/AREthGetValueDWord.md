# AREthGetValueDWord

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetValueDWord( dword objectHandle, char valuePath[] );
```

## Description

This function can be used to read out a raw value from the object specified in the objectHandle parameter. The value is accessed in this case via symbolic access paths.

## Parameters

| Name | Description |
|---|---|
| objectHandle | Handle to a AUTOSAR Eth IL object, which must be completely described in the FIBEX database.The following objects are supported. Messages Fields Method calls: Handle to a method call that was created with AREthCreateMethodCall. |
| valuePath | Access path of the value to be read out. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
