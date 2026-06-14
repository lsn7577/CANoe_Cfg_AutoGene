# on mostRawMessage

> Category: `MOST` | Type: `event`

## Syntax

```c
on mostRawMessage
```

## Description

on mostRawMessage is called on the receipt of MOST frames whose type isn't Normal.

These are RemoteRead, RemoteWrite, Alloc, Dealloc and GetSource. See Selectors for the applicable selectors. The command output(this) can be used for forwarding the message in a node chain.

If the event procedure should only react to messages on channel 1 this is defined as follows:

## Return Values

—

## Availability

| Since Version |
|---|
