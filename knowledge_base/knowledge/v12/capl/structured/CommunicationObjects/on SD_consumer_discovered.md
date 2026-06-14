# on SD_consumer_discovered

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on SD_consumer_discovered <Service>
```

## Description

The event procedure is called when a new service consumer is discovered.

## Example

```c
on SD_consumer_discovered Mirrors::MirrorAdjustment
{
  char buffer[100];
  Abstract_GetDisplayName(this.address, buffer);
  write("New consumer: %s", buffer);
}
```

## Availability

| Since Version |
|---|
