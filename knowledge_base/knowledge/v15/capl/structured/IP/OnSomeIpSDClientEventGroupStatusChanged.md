# OnSomeIpSDClientEventGroupStatusChanged

> Category: `IP` | Type: `function`

## Syntax

```c
void OnSomeIpSDClientEventGroupStatusChanged( dword serviceId, dword instanceId, dword eventGroupId, long status ); // form 1
void OnSomeIpSDClientEventGroupStatusChanged( dword serviceId, dword majorVersion, dword instanceId, dword eventGroupId, long status ); // form 2
```

## Description

This callback function can be implemented in the CAPL program if an Event Consumer (Client) wants to be notified of status changes to Event Groups.

The function is called whenever the status of an Event Group changes.

The callback function can only be called for status changes related to an Event Group that is consumed by this node.

## Parameters

| Name | Description |
|---|---|
| serviceId | ID of the service whose status has changed. |
| instanceId | Instance ID |
| eventGroupId | ID of the Event Group |
| status | 0: not subscribed 1: subscribed |
| majorVersion | Service interface major version. |

## Return Values

—

## Example

```c
void OnSomeIpSDClientEventGroupStatusChanged( dword serviceId, dword instanceId, dword eventGroupId, long status)
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1: form 1 8.5 SP4: form 2 | — | — | — | 2.0 SP2: form 1 2.0 SP3: form 2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
