# getMessageID

> Category: `CAN` | Type: `function`

## Syntax

```c
dword getMessageID(char messageName[]); // form 1
```

## Description

Finds out the message ID

## Return Values

Message ID, or (dword)-1 if the message is not found

## Example

```c
dword id;
id = GetMessageID("LightState");
```

## Availability

| Since Version |
|---|
