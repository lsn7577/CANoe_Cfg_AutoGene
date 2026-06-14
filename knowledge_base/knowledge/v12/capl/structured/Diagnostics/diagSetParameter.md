# diagSetParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetParameter (diagResponse obj, char parameterName[], double newValue)
```

## Description

Sets the numeric parameter to the specified value.

Textual diagnostic parameters cannot be set with double values.

With 7.6 SP2 the function behavior was changed. The parameter will no longer be set to its default value.

## Return Values

Error code

## Availability

| Since Version |
|---|
