# _atoi64

> Category: `Other` | Type: `function`

## Syntax

```c
int64 _atoi64(char s[]);
```

## Description

Converts the string s to a 64bit integer. The number base is decimal.

## Return Values

The converted number.
The return value is 0 if the string can’t be converted to a number. It is the largest positive/negative number in case of overflow.

## Example

```c
int64 i;
i = _atoi64("12345678901")
```

## Availability

| Since Version |
|---|
