# TestReportAddExtendedInfo

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddExtendedInfo (char type[], char text[], ...);
```

## Description

With this function, it is possible to take over information into the protocol that is not subject to processing by CANoe. This way, for example, any HTML code can be copied directly into the protocol. A corresponding type specification specifies the type of information (e.g. HTML).

## Parameters

| Name | Description |
|---|---|
| html | HTML code |
| text | Plain text without formatting instructions |
| other | other Text, taken over into the XML report, but not shown in the HTML report. |

## Return Values

—

## Availability

| Since Version |
|---|
