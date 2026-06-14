# AREthRemoveProvidedEventGroup

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthRemoveProvidedEventGroup( dword pevgHandle );
```

## Description

Removes an Event Group from a Provided Service Instance. The Event Group was previously added by AREthAddProvidedEventGroup.

The Events and Fields assigned to the Event Group are not deleted when the Event Group is closed.

## Return Values

0: The function was successfully executed

## Example

```c
on key 't'
{
  dword aep; // Application Endpoint handle
  dword psi; // provided service handle
  dword peg; // provided Eventgroup handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create service
  psi = AREthCreateProvidedServiceInstance(aep,10,1);

  // create Eventgroup
  peg = AREthAddProvidedEventGroup(psi,1);

  // ... do something here

  // remove the Eventgroup
  AREthRemoveProvidedEventGroup(peg);

  // ... Application Endpoint and provided Service Instance can still be used here
}
```

## Availability

| Since Version |
|---|
