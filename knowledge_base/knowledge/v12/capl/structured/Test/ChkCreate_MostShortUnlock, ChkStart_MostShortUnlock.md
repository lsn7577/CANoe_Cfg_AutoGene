# ChkCreate_MostShortUnlock, ChkStart_MostShortUnlock

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostShortUnlock();
```

## Description

The check function monitors the occurrence of "ShortUnlock" events.

A "ShortUnlock" event occurs if there is no interpretable signal for a brief moment on the input of the connected MOST hardware (< tUnlock, see also MOST specification) and the ring has been in a Light&Lock state before.

This check always works on events. Therefore, it will not detect a current "ShortUnlock" state, if this state has been entered before the check’s activation.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and must not be referenced

## Availability

| Since Version |
|---|
