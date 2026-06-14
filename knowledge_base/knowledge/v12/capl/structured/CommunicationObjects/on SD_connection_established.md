# on SD_connection_established

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on SD_connection_established <ServiceProvider>
```

## Description

The event procedure is called when a connection is established between a consumer and a provider.

This is a logical connection which needs not correspond e.g. to a TCP connection.

If you specify a single endpoint, the procedure is called for all connections of that endpoint and the other endpoint can be identified through the service selector of the this variable. If you specify both endpoints, the procedure is only called for the specific pair of consumer and provider and there is no this variable.

## Example

```c
on SD_connection_established Mirrors::MirrorAdjustment.consumerSide[CANoe]
{
  // subscribe event
  Abstract_SubscribeEvent(MirrorAdjustment.consumerSide[CANoe, this.service.ProviderIndex].CurrentPosition);
}
```

## Availability

| Since Version |
|---|

## Selectors

| consumedServiceRef * | ../Objects/CAPLfunctionConsumedServiceRef.htm |
|---|---|
| providedServiceRef * | ../Objects/CAPLfunctionProvidedServiceRef.htm |
