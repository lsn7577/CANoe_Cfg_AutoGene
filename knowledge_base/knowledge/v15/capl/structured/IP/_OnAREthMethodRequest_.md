# <OnAREthMethodRequest>

> Category: `IP` | Type: `function`

## Syntax

```c
void <OnAREthMethodRequest>( dword methodHandle, dword messageHandle, dword messageResponseHandle ); // form 1
void <OnAREthMethodRequest>( dword methodHandle, dword messageHandle ); // form 2
```

## Description

A callback function with this signature must be passed to the CAPL function AREthAddMethod.

This callback is called when a consumer has called the method created with AREthAddMethod.

## Parameters

| Name | Description |
|---|---|
| methodHandle | Handle of the Event that triggered the callback, see AREthAddMethod. |
| Note If the getter method of a field was overwritten (see also AREthAddField), the SOME/IP message payload of the request is empty. If the setter method of a field was overwritten (see also AREthAddField), the SOME/IP message contains the current field content. |  |
| Note If the getter method of a field was overwritten (see also AREthAddField), the SOME/IP response message contains the field content. The content of this SOME/IP message can be changed using AREthSetValue.... These changes have no effect on the field content itself when this callback method is exited. If the setter method of a field was overwritten (see also AREthAddField), the SOME/IP response message already contains the new field content. The content of this SOME/IP message can be changed using AREthSetValue.... When this callback method is exited, the current field content is automatically overwritten with the field content of the SOME/IP response message. |  |

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
