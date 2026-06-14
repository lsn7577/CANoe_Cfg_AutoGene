# linGetWakeupLength

> Category: `Obsolete` | Type: `function`

## Syntax

```c
int linGetWakeupLength (linWakeupFrame wakeupFrame)
```

## Description

With this function it is possible to retrieve a length of an occurred Wakeup frame.

## Return Values

Returns the retrieved length [in units of 10 µsec] or zero on failure.

## Example

Query the length of the wakeup frames

```c
on linWakeupFrame
{
write("Wake-up frame length: %d µs", linGetWakeupLength(this)*10);
}
```

## Availability

| Since Version |
|---|
