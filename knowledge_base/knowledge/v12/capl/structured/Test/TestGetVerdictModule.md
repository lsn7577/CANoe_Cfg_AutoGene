# TestGetVerdictModule

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetVerdictModule ();
```

## Description

Returns the current verdict out of the test module.

## Return Values

0: pass

## Example

```c
// gets the verdict of the test module and report it in the Write Window
void MainTest()
{
   MyTestCase();
   if (TestGetVerdictModule() == 1)
      Write("State of Test Module: failed.");
   else
      Write("State of Test Module: passed.");
}
```

## Availability

| Since Version |
|---|
