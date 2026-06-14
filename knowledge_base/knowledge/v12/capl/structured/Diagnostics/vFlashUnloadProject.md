# vFlashUnloadProject

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashUnloadProject();
```

## Description

Unloads the current vFlash project. The CAPL callback vFlashUnloadProjectCompleted will be called when the unloading completed and further API calls are possible.

Note: This event-driven API is only needed outside of test modules or test units.

## Return Values

—

## Example

```c
  // ...
  vFlashUnloadProject();
}

void vFlashUnloadProjectCompleted(enum vFlashStatusCode statusCode)
{
  write("Unloading project completed, another project can be loaded.");
}
```

## Availability

| Since Version |
|---|
