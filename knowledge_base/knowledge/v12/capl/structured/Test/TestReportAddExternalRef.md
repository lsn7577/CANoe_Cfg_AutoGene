# TestReportAddExternalRef

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddExternalRef(char[] type, char[] title, char[] ref); // form 1
```

## Description

Adds an external reference to the report (URL, DOORS or eASEE link), which appears as a link in the test report.

Can be used in test cases (test case functions), test groups or in MainTest functions.

## Return Values

—

## Example

```c
testcase tc_1_1()
{
   TestCaseTitle("tc_1_1", "Test Case 1.1");
 TestReportAddExternalRef("url", "Requirement", 
"doors://doorssrv:36677/?version=1,prodID=0,dbid=42d2481361dc551c,container=00004600,object=19");
   ...
}
```

## Availability

| Since Version |
|---|
