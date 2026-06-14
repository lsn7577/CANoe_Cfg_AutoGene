# callAllOnEnvVar

> Category: `Other` | Type: `function`

## Syntax

```c
void callAllOnEnvVar();
```

## Description

Calls all event procedures for environment variables (on envVar). This can be necessary at measurement start to initialize environment variables, to start timers activated in response to changes of environment variables, or to send messages on the bus with the start values of environment variables.

## Return Values

—

## Example

```c
on start
{
callAllOnEnvVar();
}
```

## Availability

| Since Version |
|---|
