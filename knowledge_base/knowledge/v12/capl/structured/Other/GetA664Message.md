# GetA664Message

> Category: `Other` | Type: `function`

## Syntax

```c
long GetA664Message (PDUobject aPDU, a664Message aMessage)
```

## Description

This function can be used within an “ON PDU”-handler to retrieve the A664Message object, to which the PDU corresponds.

The a664Message object then allows to retrieve the various runtime parameters like BAG or error flags via message selectors.

Note: the message ID is available, but not the message name.

## Availability

| Since Version |
|---|
