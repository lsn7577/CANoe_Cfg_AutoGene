# on SD_service_discovery

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on SD_service_discovery <Service>
```

## Description

The event procedure is called when service discovery is triggered by a consumer.

## Example

}

```c
on SD_service_discovery Mirrors::MirrorAdjustment
{
  dword i;
  for (i = 0; i < getNrOfCOProviders(MirrorAdjustment); ++i)
  {
    SD_AnnounceProvider(MirrorAdjustment.providerSide[this.consumer.ConsumerIndex, i]);
  }
```

## Availability

| Since Version |
|---|

## Selectors

| serviceConsumerRef * | ../Objects/CAPLfunctionServiceConsumerRef.htm |
|---|---|
