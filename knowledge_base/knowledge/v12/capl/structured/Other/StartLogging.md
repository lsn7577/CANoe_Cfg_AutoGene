# StartLogging

> Category: `Other` | Type: `function`

## Syntax

```c
void startLogging();
```

## Description

Starts all Logging Blocks immediately bypassing all logging trigger settings.

## Parameters

| Name | Description |
|---|---|
| Note If you use the function in standalone mode with VN8900/CANoe RT and if you activated logging and Trigger Block in the standalone mode configuration settings you can address the (single) Logging Block available in this case by passing an empty string as parameter. |  |

## Return Values

—

## Example

```c
startLogging();
// starts all Logging Blocks
stopLogging();
// stops all Logging Blocks
startLogging( "Logging 1");
// starts the Logging Block "Logging 1"
stopLogging( "Logging 1");
// stops the Logging Block "Logging 1"
startLogging( "Logging 1", 2000);
// starts the Logging Block "Logging 1" with pre-trigger time 2000 milliseconds.
stopLogging( "Logging 1", 1000);
// stops the Logging Block "Logging 1" with post-trigger time 1000 milliseconds.
```

## Availability

| Since Version |
|---|
