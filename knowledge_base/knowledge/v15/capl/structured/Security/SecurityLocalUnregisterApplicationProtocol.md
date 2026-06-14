# SecurityLocalUnregisterApplicationProtocol

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalUnregisterApplicationProtocol(char applicationProtocolUserDefinedId[]) // form 1
long SecurityLocalUnregisterApplicationProtocol(char applicationProtocolUserDefinedId[], dword vLanId) // form 2
```

## Description

Unregisters the reception of the application protocol with the specified User Defined Id. The node will no longer receive this application protocol and the callbacks OnSecurityLocalApplicationProtocolRxFinished or OnSecurityLocalApplicationProtocolTxFinished will also no longer be called. The call of SecurityLocalAllowNetworkWideRegistrations is a precondition for using this function.

## Example

```c
//Implement this in an Observer-Node to receive callbacks of Application-Protocol for real ECUs
on preStart
{
  long result = 0;
  result = SecurityLocalAllowNetworkWideRegistrations();
  Write(“The call of SecurityLocalAllowNetworkWideRegistrations returned %i", result);
}

on start
{
  dword result = 0;
  result = SecurityLocalRegisterApplicationProtocol("APPLICATIONPROTOCOLNAME",10);
  Write("SecurityLocalRegisterApplicationProtocol to register to APPLICATIONPROTOCOLNAME on VLAN 10 returned %i", result);
}

void OnLocalSecurityApplicationProtocolRxFinished(char applicationProtocolName[], byte payload[], dword payloadLength, dword result)
{
if(strncmp(applicationProtocolName,"APPLICATIONPROTOCOLNAME",23) == 0)
  {
    write("Received Application Protocol %s", applicationProtocolName);
  }
}

on stopMeasurement
{
  dword result = 0;
  result = SecurityLocalUnregisterApplicationProtocol("APPLICATIONPROTOCOLNAME",10);
  Write("SecurityLocalUnregisterApplicationProtocol to unregister from APPLICATIONPROTOCOLNAME on VLAN 10 returned %i", result);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 1, 2 | 13.0 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
