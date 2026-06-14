# OnAREthSDServerEventGroupStatusChangedIPv6

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAREthSDServerEventGroupStatusChangedIPv6( dword serviceId, dword majorVersion, dword instanceId, dword eventGroupId, long status, byte newIpAddress[], dword newPort );
```

## Description

This callback function can be implemented in the CAPL program if a Service Server wants to be notified whenever a Subscriber is added.

This function is called when a Client executes a subscribe eventgroup command.

## Return Values

—

## Availability

| Since Version |
|---|
