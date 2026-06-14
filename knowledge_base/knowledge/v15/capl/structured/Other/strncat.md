# strncat

> Category: `Other` | Type: `function`

## Syntax

```c
void strncat(char dest[], char src[], long len);
```

## Description

This function appends src to dest. len indicates the maximum length of the composite string. The function ensures that there is a terminating "\0". Thus, a maximum of len - strlen(dest) - 1 characters are copied.

## Parameters

| Name | Description |
|---|---|
| dest | Target string to which characters are appended. |
| src | Appended string. |
| len | Maximum length of composite string including terminating '\0'. |

## Return Values

—

## Example

```c
char s[20];
strncpy(s, "Vector", 10); // s is "Vector"
strncat(s, " CANoe", 19); // s is "Vector CANoe"
strncpy(s, "Vector", 10); // s is "Vector"
strncat(s, " CANoe", 11); // s is "Vector CAN"
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
