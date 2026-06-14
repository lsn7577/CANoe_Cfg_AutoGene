# getValueSize

> Category: `Other` | Type: `function`

## Syntax

```c
int getValueSize(EnvVarName);
```

## Description

Returns the size of the environment variable value in bytes.

## Return Values

Size of the data in bytes.

## Example

```c
int vSize;
...
// Size of the data of an environment variable of type integer
vSize = getValueSize(switch);
// Buffersize of an environment variable of type string
// (with terminating Null character)
vSize = getValueSize(nodename);
// Size of the data byffer of an environment variable of type data
vSize = getValueSize(DiagData);
...
```

## Availability

| Since Version |
|---|
