# linIsChannelMatserMode

> Category: `LIN` | Type: `function`

## Syntax

```c
long linIsChannelMasterMode()
```

## Description

This function returns 1 if the network channel given by the current bus context is running in master mode, 0 otherwise. See SetBusContext for how to change the current bus context.

The channel’s master mode setting can be changed at any time using the function linSetChannelMasterMode.

See also Master Mode of the LIN Hardware for details on the LIN channel master mode.

## Return Values

1 if the current bus context’s LIN channel is in master mode, 0 otherwise

## Example

```c
if (!linIsChannelMasterMode())
{
  // manually activate Master mode on LIN hardware
  linSetChannelMasterMode(1);
}
```

## Availability

| Since Version |
|---|
