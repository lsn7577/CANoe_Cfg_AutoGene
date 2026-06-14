# TestGetVerdictLastTestCase

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetVerdictLastTestCase();
```

## Description

Returns the verdict of the last elapsed or current test case.

## Return Values

0: pass

## Example

```c
// gets the verdict of last test case and report it in the Write Window
void MainTest()
{
   MyTestCase();
   if (TestGetVerdictLastTestCase() == 1)
      Write("MyTestCase failed.");
   else
      Write("MyTestCase passed.");
}
```

## Availability

| Since Version |
|---|
