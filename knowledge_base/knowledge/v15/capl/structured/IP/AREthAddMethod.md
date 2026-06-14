# AREthAddMethod

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthAddMethod( dword psiHandle, dword methodId, char onMethodRequestCallback[] ); // form 1
dword AREthAddMethod( dword psiHandle, dword methodId, char onMethodRequestCallback[], long fireAndForget); // form 2
```

## Description

This function adds a method to a Provided Service Instance that was created with AREthCreateProvidedServiceInstance.

If this method is called by a client through a SOME/IP request, the specified CAPL callback function is called. Only one CAPL callback function can be registered for each method.

A method can be removed again using the AREthRemoveMethod function.

## Parameters

| Name | Description |
|---|---|
| psiHandle | Handle of the Provided Service Instance that was created by AREthCreateProvidedServiceInstance. |
| methodId | Identifier of the method |
| onMethodRequestCallback | Name of the CAPL callback function, see CAPL callback <OnAREthMethodRequest> |
| fireAndForget | Specifies whether the provider is to send a response after the method call: 1: A response is not sent 0: A response is sent (default behavior) |

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
