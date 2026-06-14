# ChkCreate_MostCriticalUnlock, ChkStart_MostCriticalUnlock

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostCriticalUnlock();
```

## Description

The check function monitors the occurrence of "CriticalUnlock" events.

A "CriticalUnlock" event is generated as soon an unlock occurs after a "Stable Lock" condition, which is longer than tUnlock (70 ms), or several unlocks occur successively, which together are longer than tUnlock (see MOST specification for more information).

This check always works on events. Therefore, it will not detect a current "CriticalUnlock" state, if this state has been entered before the check’s activation.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and must not be referenced

## Availability

| Since Version |
|---|
