# AREthCreateMethodCall

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthCreateMethodCall( dword csiHandle, dword methodId, char OnAREthMethodResponse [] ); // form 1
dword AREthCreateMethodCall( dword csiHandle, dword methodId ); // form 2
dword AREthCreateMethodCall( dword csiHandle, dword methodId, char OnAREthMethodResponse [], char OnAREthMethodError []); // form 3
```

## Description

This function creates a method call for the consumer. By means of the return value of the function, the method parameters can be set using AREthSetValue.... The method is then called using AREthCallMethod.

The syntax specified in form 2 must be used if the fireAndForget parameter was used when the method was created for the provider (see also AREthAddMethod).

The method call can be removed again using the AREthRemoveMethodCall function.

## Parameters

| Name | Description |
|---|---|
| csiHandle | Handle of the Consumed Service Instance that was created by AREthCreateConsumedServiceInstance. |
| methodId | Identifier of the method |
| onResponseCallback | This callback function is called when the response is received, see <OnAREthMethodResponse> |
| onErrorCallback | This callback function is called when a SomeIp error message is received, see <OnAREthMethodError> |

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters Member_value1 and Member_value2, and a return parameter Result.

```c
variables
{
  dword gMc; // global method call handle
}

void Initialize()
{
  dword aep; // Application Endpoint handle
  dword csi; // consumed Service Instance handle

  // open Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(0x11, 50002);

  // cretae Service Instance
  csi = AREthCreateConsumedServiceInstance(aep,11,1);

  // create method call
  gMc = AREthCreateMethodCall(csi,31,"OnMethodResponse");
}

on key 's'
{
  // if this key is pressed the method should be called

  // set the two input parameters of the method
  AREthSetValueDWord(gMc,"Member_value1",11);
  AREthSetValueDWord(gMc,"Member_value2",22);

  // call the method
  AREthCallMethod(gMc);
}

void OnMethodResponse(dword methodCallHandle, dword messageResponseHandle )
{
  dword res; // value of return parameter

  // get the returned parameter values
  res = AREthGetValueDWord(messageResponseHandle,"Result");

  write("The method call returned value: %d",res);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2: form 1, 2 14: form 3 | — | — | — | 2.1 SP3: form 1, 2 5.0 SP3: form 3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
