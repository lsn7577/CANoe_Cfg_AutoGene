# ChkCreate_MostStableLock, ChkStart_MostStableLock

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostStableLock(Callback aCallback);
```

## Description

The check function monitors the occurrence of "StableLock" events.

A "StableLock" event is generated as soon as the hardware has been in the "Lock" condition for a period of time equal to or longer than tLock (see MOST Specification V 2.4), provided that no "Unlock" events have occurred.

This check always works on events. Therefore, it will not detect a current "StableLock" state, if this state has been entered before the check’s activation.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and must not be referenced

## Availability

| Since Version |
|---|
