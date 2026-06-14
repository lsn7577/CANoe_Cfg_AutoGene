# getAttribute

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
getAttribute(attributable object, attribute int32 attribute, long& value); // form 1
getAttribute(attributable object, attribute uint32 attribute, dword& value); // form 2
getAttribute(attributable object, attribute int64 attribute, int64& value); // form 3
getAttribute(attributable object, attribute uint64 attribute, qword& value); // form 4
getAttribute(attributable object, attribute double attribute, double& value); // form 5
getAttribute(attributable object, attribute string attribute, char value[]); // form 6
getAttribute(attributable object, char attribute[], long& value); // form 7
getAttribute(attributable object, char attribute[], dword& value); // form 8
getAttribute(attributable object, char attribute[], int64& value); // form 9
getAttribute(attributable object, char attribute[], qword& value); // form 10
getAttribute(attributable object, char attribute[], double& value); // form 11
getAttribute(attributable object, char attribute[], char value[]); // form 12
```

## Description

Reads an attribute value from an attributable object.

## Parameters

| Name | Description |
|---|---|
| object | Attributable object at which the attribute value is read. |
| attribute | Attribute or attribute name for which the value is read. |
| value | Out-parameter for the attribute value. |

## Example

```c
// vCDL
version 1.4;
namespace SomeNamespace
{
  [Binding="Abstract"]
  object SomeObject {}
}

// CAPL
on start
{
  char str[100];
  getAttribute(SomeObject, _SystemAttributes::Binding, str);
  write("Binding: %s", str);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 | 15 | 15 | 15 | 6 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
