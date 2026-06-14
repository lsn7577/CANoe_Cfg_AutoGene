# TestReportAddExternalRef

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddExternalRef(char[] type, char[] title, char[] ref); // form 1
TestReportAddExternalRef(char[] type, char[] title, char[] ref, char[] owner); // form 2
```

## Description

Adds an external reference to the report (URL, DOORS or eASEE link), which appears as a link in the test report.

Can be used in test cases (test case functions), test groups or in MainTest functions.

## Parameters

| Name | Description |
|---|---|
| type | "url" for any kinds of URLs, "doors" for links to DOORS, "easee" for links to eASEE. |
| title | Text with which the link generated in the test report is displayed. If not indicated the URL indicated in ref is used. |
| ref | The URL of the external resource, which is referenced. |
| owner | This attribute is intended to be used by applications which maintain links to external resources automatically so they can identify their external reference elements. It’s recommended not to use it individually. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0: form 1 7.5: form 2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
