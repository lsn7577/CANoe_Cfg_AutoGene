# on mostAMSMessage

> Category: `MOST` | Type: `event`

## Syntax

```c
on mostAMSMessage
```

## Description

The event procedure on mostAMSMessage is called when a message is received from the Application Message Service (AMS).

The key word this and the message selectors are available within event procedures to permit access to the data of the message just received. The output(this) command serves to pass the message in a nodal sequence.

The same modes of the event procedure as for on mostMessage may be used to prefilter messages.

## Return Values

—

## Availability

| Since Version |
|---|
