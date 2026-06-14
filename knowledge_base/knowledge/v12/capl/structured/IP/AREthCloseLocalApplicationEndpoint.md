# AREthCloseLocalApplicationEndpoint

> Category: `IP` | Type: `function`

## Syntax

```c
LONG AREthCloseLocalApplicationEndpoint( dword aepHandle );
```

## Description

Closes an Application Endpoint that was previously opened with AREthOpenLocalApplicationEndpoint.

Services and the objects assigned to the services (Eventgroups, Events, Fields, and Methods) are removed when the Application Endpoint is closed. If the Application Endpoint has to be reopened, all objects must be created again.

## Return Values

0: The function was successfully executed

## Example

```c
on key 't'
{
  dword aep; // Application Endpoint handle

  // open an Application Endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // ... do something here

  // close the Application Endpoint
  AREthCloseLocalApplicationEndpoint(aep);
}
```

## Availability

| Since Version |
|---|
