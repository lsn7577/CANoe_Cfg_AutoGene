# mostRcvSpyMessagesOnly

> Category: `MOST` | Type: `function`

## Syntax

```c
mostRcvSpyMessagesOnly ()
```

## Description

The MOST message handling routines of this node are only called if the message was received by the Spy of the bus interfaces.

This mode is especially useful for nodes that act as pure observers or – with the help of the Spy – are used to perform cross-node analyses.

Queries such as "if (!this.MOST_IsSpy) return;" have been eliminated in the message handling routines, because the message handling routines are no longer called by node and Spy messages.

## Return Values

—

## Availability

| Since Version |
|---|
