# Abstract_CreateAddress

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
addressHandle Abstract_CreateAddress(CommunicationObject co, char[] name)
```

## Description

Creates a pseudo address for a communication object endpoint if abstract binding is used. The address can be attached to an endpoint with SD_SetAddress. For abstract binding, the address of an endpoint actually does not contain more information than a name which can be retrieved again through Abstract_GetDisplayName.

The address is necessary for implementation of service discovery; e.g. in the handlers on SD_consumer_discovered and on SD_provider_discovered, the address is passed as a selector.

## Return Values

—

## Example

```c
SD_SetAddress(newProvider, Abstract_CreateAddress(MirrorAdjustment, "RearMirror"), MirrorAdjustment[CANoe]);
```

## Availability

| Since Version |
|---|
