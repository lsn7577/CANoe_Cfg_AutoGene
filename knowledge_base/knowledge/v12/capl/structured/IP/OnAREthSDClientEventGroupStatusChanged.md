# OnAREthSDClientEventGroupStatusChanged

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAREthSDClientEventGroupStatusChanged( dword serviceId, dword instanceId, dword eventGroupId, long status );
```

## Description

This callback function can be implemented in the CAPL program if an Event Consumer (Client) wants to be notified of status changes to Event Groups.

The function is called whenever the status of an Event Group changes.

The callback function can only be called for status changes related to an Event Group that is consumed by this node.

## Return Values

—

## Example

```c
void OnAREthSDClientEventGroupStatusChanged( dword serviceId, dword instanceId, dword eventGroupId, long status)
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
