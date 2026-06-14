# SomeIpOpenLocalApplicationEndpoint

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpOpenLocalApplicationEndpoint( dword transportProtocol, dword port ); // form 1
```

## Description

Opens an endpoint for SOME/IP Remote Procedure CallRPC messages.

An endpoint represents a socket. The IP address is the IP address of the current interface, which is determined by the bus context.

Services can be assigned to an Application Endpoint using the SomeIpCreateProvidedServiceInstance or SomeIpCreateConsumedServiceInstance function. An Application Endpoint can be closed again using the SomeIpCloseLocalApplicationEndpoint function.

This only works with the node TCP/IP stack; in the Windows TCP/IP stack the interface cannot be determined by the bus context.

The SOME/IP Service DiscoverySD endpoints can be configured using the properties of SOME/IP IL (see also: SomeIpSetProperty).

## Return Values

0: An error occurred. The error can be evaluated using the SomeIpGetLastError function.

## Example

```c
void Initialize()
{
  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle
  DWORD peg; // provided Eventgroup handle
  DWORD pev; // provided Event handle

  // open Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

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

| Since Version |
|---|
