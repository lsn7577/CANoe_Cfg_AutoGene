# OnAREthSDServerEventGroupStatusChanged

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAREthSDServerEventGroupStatusChanged( dword serviceId, dword instanceId, dword eventGroupId, long status, dword newIpAddress, dword newPort ); // form 1
void OnAREthSDServerEventGroupStatusChanged( dword serviceId, dword majorVersion, dword instanceId, dword eventGroupId, long status, dword newIpAddress, dword newPort ); // form 2
```

## Description

This callback function can be implemented in the CAPL program if a Service Server wants to be notified whenever a Subscriber is added.

This function is called when a Client executes a subscribe eventgroup command.

## Parameters

| Name | Description |
|---|---|
| serviceId | ID of the service whose status has changed. |
| instanceId | Instance ID |
| eventGroupId | ID of the Event Group. |
| status | 0: not subscribed 1: subscribed |
| newIpAddress | IPv4 address via which the subscription was received. |
| newPort | Source port via which the subscription was received. |
| majorVersion | Service interface major version. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
