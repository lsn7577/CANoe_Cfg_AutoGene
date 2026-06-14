# linInitBegin

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linInitBegin();
```

## Description

Starts the CAPL-controlled LIN initialization procedure.

After initialization has been completed linInitEnd() must be called.

## Return Values

0: Initialization is not possible.In this case initialization should not be continued.

## Availability

| Up to Version |
|---|
