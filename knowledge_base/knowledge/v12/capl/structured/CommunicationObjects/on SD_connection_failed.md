# on SD_connection_failed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on SD_connection_failed <ServiceProvider>
```

## Description

The event procedure is called when a connection attempt between a consumer and a provider fails.

This is a logical connection which needs not correspond e.g. to a TCP connection.

If you specify a single endpoint, the procedure is called for all connections of that endpoint and the other endpoint can be identified through the address selector of the this variable. If you specify both endpoints, the procedure is only called for the specific pair of consumer and provider and there is no this variable.

## Example

```c
on SD_connection_failed Mirrors::MirrorAdjustment.consumerSide[CANoe]
{
  char buffer[100];
  Abstract_GetDisplayName(this.address, buffer);
  write("Connection failed with %s", buffer);
}
```

## Availability

| Since Version |
|---|
