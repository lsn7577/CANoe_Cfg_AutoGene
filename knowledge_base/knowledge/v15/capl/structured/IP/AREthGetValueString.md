# AREthGetValueString

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetValueString( dword objectHandle, char valuePath[], dword bufferLength, char buffer[] );
```

## Description

This function can be used to read out a string from the object specified in the objectHandle parameter.

For Enum data types, the function returns the symbolic value.

## Parameters

| Name | Description |
|---|---|
| objectHandle | Handle to a AUTOSAR Eth IL object, which must be completely described in the FIBEX database.The following objects are supported: Messages Fields Method calls: Handle to a method call that was created with AREthCreateMethodCall. |
| valuePath | Path of the value to be read out.For specification of complex paths, a corresponding syntax must be adhered to. |
| bufferLength | Length of the buffer parameter in bytes.If the selected buffer length is too small, the function copies only the number of characters (including null termination) that fit in the buffer. |
| buffer | After execution, this parameter contains the null-terminated string. See BOM in SOME/IP UTF8 and UTF16 strings |

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
