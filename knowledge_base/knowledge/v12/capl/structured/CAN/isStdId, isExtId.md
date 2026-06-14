# isStdId, isExtId

> Category: `CAN` | Type: `function`

## Syntax

```c
long isStdId(dword id);
```

## Description

Checks parameter for extended identifier (29 bit) or standard identifier (11 Bit).

## Return Values

1 if check was successful, else 0

## Example

```c
...
if(isExtId(this))
write("extended identifier");
else
write("standard identifier");
or
std = isStdId(m100.id);
```

## Availability

| Since Version |
|---|
