# valOfId

> Category: `CAN` | Type: `function`

## Syntax

```c
long valOfId(dword id);
```

## Description

Returns the value of a message identifier independent of its type.

Identifier as long value.

## Return Values

Identifier as long value.

## Example

```c
on message *
{
long x;
x = valOfId(this);
write("Received Identifier: %d",x);
output(this);
}
```

## Availability

| Since Version |
|---|
