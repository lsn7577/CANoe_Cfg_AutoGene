# OnAREthSDServerEventGroupStatusChanged

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAREthSDServerEventGroupStatusChanged( dword serviceId, dword instanceId, dword eventGroupId, long status, dword newIpAddress, dword newPort ); // form 1
```

## Description

This callback function can be implemented in the CAPL program if a Service Server wants to be notified whenever a Subscriber is added.

This function is called when a Client executes a subscribe eventgroup command.

## Return Values

—

## Example

```c
void OnAREthSDServerEventGroupStatusChanged( dword serviceId, dword instanceId, dword eventGroupId, long status, dword newIpAddress, dword newPort)
{
  char buffer[100];
  if(status == 0)
  {
    snprintf(buffer,elcount(buffer),"not subscribed");
  }
  else if(status == 1)
  {
    snprintf(buffer,elcount(buffer),"subscribed");
  }
  else
  {
    snprintf(buffer,elcount(buffer),"Undefined status");
  }
  write("Event group (ID %d), of service %d (instance %d): %s",eventGroupId,serviceId,instanceId,buffer);
}
```

## Availability

| Since Version |
|---|
