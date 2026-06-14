# mkExtId

> Category: `CAN` | Type: `function`

## Syntax

```c
dword mkExtId(dword id);
```

## Description

Returns an extended id.

## Return Values

Extended identifier

## Example

```c
...
msg.id = mkExtId(this.id);
...
```

## Availability

| Since Version |
|---|
