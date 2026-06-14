# DoIP_ForceLocalUDPSendPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_ForceLocalUDPSendPort(dword forcedPort);
```

## Description

According to ISO 13400, the local send port for UDP messages should be dynamically selected. This function allows forcing the local UDP send port to a specific value, typically to 13400 to indicate DoIP.

Note that specifying a "well-known" or system port (1..1023) might not work on most systems.

## Return Values

Error code

## Example

```c
On preStart
{
  // Make sure that in an ECU simulation all UDP packets are sent from the standard port
  DoIP_ForceLocalUDPSendPort(13400);
}
```

## Availability

| Since Version |
|---|
