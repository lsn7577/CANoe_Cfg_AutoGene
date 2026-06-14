# vFlashReprogram

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashReprogram();
```

## Description

Starts the flashing procedure. The progress will be indicated by calls to the optional callback vFlashProgramProgressCallback. The procedure has finished when CAPL callback vFlashReprogramCompleted is called.

Note: This event-driven API is only needed outside of test modules or test units.

## Return Values

1: Flashing was started

## Example

```c
  FlashReprogram();
}
void vFlashProgramProgressCallback(dword progressInPercent, dword remainingTimeInS)
{
  // Do not print on every progress callback, but only in 10% steps
  DWORD sProgress = 0;
  if (progressInPercent < sProgress)
    sProgress = 0; // reset progress stored
  if (progressInPercent < 100 && (progressInPercent - sProgress) >= 10)
  {
    write("Progress: %3u%%, %us remaining", progressInPercent, remainingTimeInS);
    sProgress = progressInPercent - (progressInPercent % 10);
  }
}

void vFlashReprogramCompleted(long status)
{
  write("Reprogramming completed with status %d", status);
}
```

## Availability

| Since Version |
|---|
