# on SD_connection_requested

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on SD_connection_requested <ServiceProvider>
```

## Description

The event procedure is called when a connection is requested by a consumer.

This is a logical connection which needs not correspond e.g. to a TCP connection.

## Example

```c
on SD_connection_requested Mirrors::MirrorAdjustment.providerSide[LeftMirror]
{
  // react on the request with connection establishment
  SD_ConnectAsync(MirrorAdjustment.providerSide[this.consumer.ConsumerIndex, LeftMirror]);
}
```

## Availability

| Since Version |
|---|

## Selectors

| serviceConsumerRef * | ../Objects/CAPLfunctionServiceConsumerRef.htm |
|---|---|
