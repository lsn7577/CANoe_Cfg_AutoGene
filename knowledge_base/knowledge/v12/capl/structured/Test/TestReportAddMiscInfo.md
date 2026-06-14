# TestReportAddMiscInfo

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddMiscInfo (char name[], char description[], ...);
```

## Description

With these functions, information pairs of name and description (e.g. "parameter value V0" and "3.7 V") can be taken up into an additional information area in the report. The additional information area must be created previously with TestReportAddMiscInfoBlock. If this function is used and there is no corresponding information area, then a warning will be generated in the Write Window and a new information area will be created automatically. In this information area, any number of information pairs can be written with this function.

## Return Values

—

## Availability

| Since Version |
|---|
