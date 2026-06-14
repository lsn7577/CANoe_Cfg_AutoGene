# AREthOpenLocalApplicationEndpoint

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthOpenLocalApplicationEndpoint( dword transportProtocol, dword port ); // form 1
```

## Description

Opens an application endpoint. An endpoint represents a socket. The IP address is the IP address of the current interface, which is determined by the bus context.

Services can be assigned to an Application Endpoint using the AREthCreateProvidedServiceInstance or AREthCreateConsumedServiceInstance function. An Application Endpoint can be closed again using the AREthCloseLocalApplicationEndpoint function.

This only works with the node TCP/IP stack; in the Windows TCP/IP stack the interface cannot be determined by the bus context.

The Service DiscoverySD endpoints can be configured using the properties of AUTOSAR Eth IL (see also: AREthSetProperty).

## Return Values

0: An error occurred. The error can be evaluated using the AREthGetLastError function.

## Example

Example

```c
void Initialize()
{
  dword aep; // Application Endpoint handle
  dword psi; // provided service handle
  dword peg; // provided Eventgroup handle
  dword pev; // provided Event handle

  // open Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create Service Instance
  psi = AREthCreateProvidedServiceInstance(aep,10,1);
  // create Eventgroup
  peg = AREthAddProvidedEventGroup(psi,1);

  // create Event and add Event to Eventgroup
  pev = AREthAddEvent(psi, 1, "OnPrepareEvent1");
  AREthAddEventToEventgroup(peg, pev);

  // ensure that Event is sent cyclically
  AREthSetProperty(pev,"CycleTimeMs",1000);
}

void OnPrepareEvent1(dword eventHandle, dword messageHandle)
{
  // this function is called before the Event is sent. Parameters
  // can be specified here.
}
```

## Availability

| Since Version |
|---|
