# C2xIsMsgEnabled

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xIsMsgEnabled (char* dbMessage);
```

## Description

Check if a message is enabled for cyclic sending.

## Return Values

0 = true

## Example

```c
LONG result = 0;
result = C2xIsMsgEnabled("CAM");
```

## Availability

| Since Version |
|---|
