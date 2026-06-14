# SecurityLocalAllowNetworkWideRegistrations

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalAllowNetworkWideRegistrations()
```

## Description

Allows to register and unregister to network related security data. It is a precondition for using SecurityLocalRegisterApplicationProtocol and SecurityLocalUnregisterApplicationProtocol.

For use with a simulation node, the function has to be called in the on prestart event of the simulation node which is not defined in the database. The function can’t be executed after measurement has started. The function can’t be executed by database nodes.

For use with a test module, the function can be called at any time.

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
| Since Version | — | 13.0 | 13.0 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
