# vFlashLoadProject

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashLoadProject(char projectPath[]);
```

## Description

Loads the provided vFlash project stored under given path. A call to CAPL callback function vFlashLoadProjectCompleted will indicate that the project was loaded. Further API calls are only allowed after callback was called!

Note: This event-driven API is only needed outside of test modules or test units.

## Return Values

—

## Example

```c
  //...
  vFlashLoadProject("Firmware1.vflashpack");
}

void vFlashLoadProjectCompleted(long statusCode)
{
  write("Loading of project completed with status %d", statusCode);
}
```

## Availability

| Since Version |
|---|
