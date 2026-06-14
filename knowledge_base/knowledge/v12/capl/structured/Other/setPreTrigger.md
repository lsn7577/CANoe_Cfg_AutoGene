# setPreTrigger

> Category: `Other` | Type: `function`

## Syntax

```c
setPreTrigger(long preTriggerTime);
```

## Description

Sets the pretrigger of the logging. The pretrigger set with this function is valid until the end of the measurement or until the next call of this function.

Note: The function startLogging() does not consider the setting with function setPreTrigger, use the CAPL function trigger() instead.

## Example

```c
on start
{
  SetPreTrigger(5000);
  SetPostTrigger(5000);
}

on key 'x'
{

    //start and stop of all CAPL trigger/Logging blocks with pre and post trigger settings
  trigger();
}
```

## Availability

| Since Version |
|---|
