# getLocalTimeString

> Category: `Other` | Type: `function`

## Syntax

```c
void getLocalTimeString(char timeBuffer[]);
```

## Description

Copies a printed representation of the current date and time into the supplied character buffer. The format of the string is ddd mmm dd hh:mm:ss jjjj (e.g. "Fri Aug 21 15:22:24 1998").

## Return Values

—

## Example

```c
...
char timeBuffer[64];

getLocalTimeString(timeBuffer);
// now timeBuffer contains for example. "Fri Aug 21 15:22:24 1998"
...
```

## Availability

| Since Version |
|---|
