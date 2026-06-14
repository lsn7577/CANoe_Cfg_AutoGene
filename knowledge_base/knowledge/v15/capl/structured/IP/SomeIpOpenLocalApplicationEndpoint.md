# SomeIpOpenLocalApplicationEndpoint

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpOpenLocalApplicationEndpoint( dword transportProtocol, dword port ); // form 1
dword SomeIpOpenLocalApplicationEndpoint( dword transportProtocol, dword port, dword ipv4Address ); // form 2
dword SomeIpOpenLocalApplicationEndpoint( dword transportProtocol, dword port, byte ipv6Address[] ); // form 3
dword SomeIpOpenLocalApplicationEndpoint( IP_Endpoint localIPEndpoint); // form 4
```

## Description

Opens an endpoint for SOME/IP Remote Procedure CallRPC messages.

An endpoint represents a socket. The IP address is the IP address of the current interface, which is determined by the bus context.

Services can be assigned to an Application Endpoint using the SomeIpCreateProvidedServiceInstance or SomeIpCreateConsumedServiceInstance function. An Application Endpoint can be closed again using the SomeIpCloseLocalApplicationEndpoint function.

## Parameters

| Name | Description |
|---|---|
| transportProtocol | 6: TCP 17: UDP |
| port | UDP: Port on which the messages can be both sent and received. TCP: Port on which the messages can be either sent or received.If a node is to receive and send messages, two Application Endpoints must be set up: one for the receive direction and the other for the send direction. |
| ipv4Address | Bind the socket to this IPv4 address. The address should be given in network byte order. |
| ipv6Address | Bind the socket to this IPv6 address. The 16 bytes in the array should be given in network byte order. |
| localIPEndpoint | Object of type IP_Endpoint that contains the address/port of the local endpoint. |

## Example

```c
void Initialize()
{
  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle
  DWORD peg; // provided Eventgroup handle
  DWORD pev; // provided Event handle

  // open Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(IP_Endpoint(UDP:192.168.0.1:50002));

  // create Service Instance
  psi = SomeIpCreateProvidedServiceInstance(aep,10,1);
  // create Eventgroup
  peg = SomeIpAddProvidedEventGroup(psi,1);

  // create Event and add Event to Eventgroup
  pev = SomeIpAddEvent(psi, 1, "OnPrepareEvent1");
  SomeIpAddEventToEventgroup(peg, pev);

  // ensure that Event is sent cyclically
  SomeIpSetProperty(pev,"CycleTimeMs",1000);
}

void OnPrepareEvent1(DWORD eventHandle, DWORD messageHandle)
{
  // this function is called before the Event is sent. Parameters
  // can be specified here.
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1: form 1 9.0: form 2-3 12.0 SP2: form 4 | — | — | — | 2.0 SP2: form 1 2.1: form 2-3 4.0 SP2: form 4 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
