# SomeIpRemoveProvidedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpRemoveProvidedEventGroup( dword pevgHandle );
```

## Description

Removes an Event Group from a Provided Service Instance. The Event Group was previously added by SomeIpAddProvidedEventGroup.

The Events and Fields assigned to the Event Group are not deleted when the Event Group is closed.

## Return Values

0: The function was successfully executed

## Example

```c
on key 't'
{
  DWORD aep; // Application Endpoint handle
  DWORD psi; // provided service handle
  DWORD peg; // provided Eventgroup handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = SomeIpCreateProvidedServiceInstance(aep,10,1);

  // create Eventgroup
  peg = SomeIpAddProvidedEventGroup(psi,1);

  // ... do something here

  // remove the Eventgroup
  SomeIpRemoveProvidedEventGroup(peg);

  // ... Application Endpoint and provided Service Instance can still be used here
}
```

## Availability

| Since Version |
|---|
