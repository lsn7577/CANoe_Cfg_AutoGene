# TestCaseSkipped

> Category: `Test` | Type: `function`

## Syntax

```c
TestCaseSkipped(char[] ident, char[] title);
```

## Description

This function can be used to mark a test case as unexecuted. This will then appear as a "skipped" test case in the Test Report.The verdict of the test module is not affected. This function may only be called in the context of the MainTest function.

## Return Values

—

## Example

test case "tc3" is only executed under certain conditions

```c
MainTest
{
   tc1();
   tc2();
   if(condition)
   {
      tc3();
   }
   else
   {
      TestCaseSkipped("TC3", "Example");
   }
   tc4();
}
```

## Availability

| Since Version |
|---|
