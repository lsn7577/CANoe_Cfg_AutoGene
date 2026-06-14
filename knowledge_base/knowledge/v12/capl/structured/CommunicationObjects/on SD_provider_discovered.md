# on SD_provider_discovered

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on SD_provider_discovered <Service>
```

## Description

The event procedure is called when a new service provider is discovered.

## Example

```c
on SD_provider_discovered Mirrors::MirrorAdjustment
{
  char buffer[100];
  Abstract_GetDisplayName(this.address, buffer);
  write("New provider: %s", buffer);
}
```

## Availability

| Since Version |
|---|
