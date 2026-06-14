# Syntax for Database-based Access Paths

> Category: `IP` | Type: `notes`

## Description

The path begins with a SOME/IP parameter name. Arrays of a struct/unions are selected with Name, arrays of arrays are selected with [Index].

| Example paramName.memberName.twoDimArray[1][2].fieldName |
|---|

| Parameter | Type | Description |
|---|---|---|
| GetValue(path, int32) GetValue(path, int64) | Boolean Integer Enumerated | Array value |
| Union | Index of the sub-element |  |
| Array | Number of sub-elements |  |
| GetValue(path, double) | Float Double | Array value |
| GetValue(path, len, buffer) | Enumerated | Symbolic value of the array |
| String | Array value |  |
| Union | Name of the current sub-element |  |
| SetValue(path, int32) SetValue(path, int64) | Boolean Integer Enumerated | Array value |
| SetValue(path, double) | Float Double | Array value |
| SetValue(path, len, buffer) | Enumerated | Symbolic value of the array |
| String | Array value |  |

| Version 15© Vector Informatik GmbH |
|---|
