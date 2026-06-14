# testValidateDiagAuthGeneric, testValidateDiagAuth

> Category: `Test` | Type: `function`

## Syntax

```c
long testValidateDiagAuthGeneric( const char ecuQualifier, const char genericString); // form 1
```

## Description

Initiates the diagnostics authentication process and waits until this process has (generic) completed. The test step is then evaluated as passed or failed, depending on the result, and documented in the report.

## Return Values

On success 0, otherwise error code

## Availability

| Since Version |
|---|
