# DoIP_ForceLocalTCPSendPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_ForceLocalTCPSendPort(dword forcedPort);
```

## Description

Forces local TCP send port to a specific value. According to ISO13400, the local send port for outgoing TCP connections should be dynamically selected. This function allows forcing the local TCP send port to a specific value, typically to 13400 to indicate DoIP. Note that specifying a well-known or system port (1..1023) might not work on most systems.

## Return Values

0: success-10: invalid parameterother: reserved

## Example

```c
On preStart
{
  // Make sure that tester starts TCP connection from the standard port
  DoIP_ForceLocalTCPSendPort(13400);
}
```

## Availability

| Since Version |
|---|
