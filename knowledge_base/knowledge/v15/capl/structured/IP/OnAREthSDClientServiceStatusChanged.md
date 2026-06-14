# OnAREthSDClientServiceStatusChanged

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAREthSDClientServiceStatusChanged( dword serviceId, dword instanceId, LONG status );
```

## Description

This callback function can be implemented in the CAPL program, if the Client wants to be notified of status changes to the services.

The function is called when the status of a service changes.

The callback is called regardless of whether or not the service is consumed by AREthCreateConsumedServiceInstance.

## Parameters

| Name | Description |
|---|---|
| serviceId | ID of the service whose status has changed. |
| instanceId | Instance ID |
| status | 0: down 1: up |

## Return Values

—

## Example

```c
void OnAREthSDClientServiceStatusChanged( dword serviceId, dword majorVersion, dword instanceId, LONG status)
{
  char buffer[100];
  if(status == 0)
  {
    snprintf(buffer,elcount(buffer),"Service down");
  }
  else if(status == 1)
  {
    snprintf(buffer,elcount(buffer),"Service up");
  }
  else
  {
    snprintf(buffer,elcount(buffer),"Undefined status");
  }
  write("Service %d (instance %d, major version %d): %s",serviceId,instanceId,majorVersion,buffer);
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
