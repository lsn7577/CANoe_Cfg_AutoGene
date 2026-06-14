# vFlashGetLastErrorMessage

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashGetLastErrorMessage();
```

## Description

Requests a call to the CAPL callback vFlashErrorMessage containing information on the error that occurred.

## Return Values

—

## Example

```c
  // ...Error occurred...
  vFlashGetLastErrorMessage();
}

void vFlashErrorMessage(char errorMsg[])
{
  write("Error %s", errorMsg);
}
```

## Availability

| Since Version |
|---|
