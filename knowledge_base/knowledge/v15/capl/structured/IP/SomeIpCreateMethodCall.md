# SomeIpCreateMethodCall

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpCreateMethodCall( dword csiHandle, dword methodId, char onSomeIpMethodResponse [] ); // form 1
dword SomeIpCreateMethodCall( dword csiHandle, dword methodId ); // form 2
dword SomeIpCreateMethodCall( dword csiHandle, dword methodId, char onSomeIpMethodResponse [], char onSomeIpMethodError []) ); // form 3
```

## Description

This function creates a method call for the consumer. By means of the return value of the function, the method parameters can be set using SomeIpSetValue.... The method is then called using SomeIpCallMethod.

The syntax specified in form 2 must be used if the fireAndForget parameter was used when the method was created for the provider (see also SomeIpAddMethod).

The method call can be removed again using the SomeIpRemoveMethodCall function.

## Parameters

| Name | Description |
|---|---|
| csiHandle | Handle of the Consumed Service Instance that was created by SomeIpCreateConsumedServiceInstance. |
| methodId | Identifier of the method |
| onResponseCallback | This callback function is called when the response is received, see <OnSomeIpMethodResponse> |
| onErrorCallback | This callback function is called when a SomeIp error message is received, see <OnSomeIpMethodError>. |

## Example

In this example, it is assumed that the created method is contained in the FIBEX database that is assigned to the CANoe configuration. The method has the Method ID 31, two input parameters Member_value1 and Member_value2, and a return parameter Result.

```c
variables
{
  DWORD gMc; // global method call handle
}

void Initialize()
{
  DWORD aep; // Application Endpoint handle
  DWORD csi; // consumed Service Instance handle

  // open Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(0x11, 50002);

  // cretae Service Instance
  csi = SomeIpCreateConsumedServiceInstance(aep,11,1);

  // create method call
  gMc = SomeIpCreateMethodCall(csi,31,"OnMethodResponse");
}

on key 's'
{
  // if this key is pressed the method should be called

  // set the two input parameters of the method
  SomeIpSetValueDWord(gMc,"Member_value1",11);
  SomeIpSetValueDWord(gMc,"Member_value2",22);

  // call the method
  SomeIpCallMethod(gMc);
}

void OnMethodResponse(dword methodCallHandle, dword messageResponseHandle )
{
  DWORD res; // value of return parameter

  // get the returned parameter values
  res = SomeIpGetValueDWord(messageResponseHandle,"Result");

  write("The method call returned value: %d",res);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1: form 1, 2 14: form 3 | — | — | — | 2.0 SP2: form 1, 2 5.0 SP3: form 3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
