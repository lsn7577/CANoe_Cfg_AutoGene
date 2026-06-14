# File Search Procedure

> Category: `Other` | Type: `notes`

## Description

A file search procedure is used to determine the absolute file path. There are different procedures for writing and reading files.

In a distributed simulation environment (CANoe RT or VN8900) it is required to pre-define all files to be read in CAPL programs in the CANoe simulation or test setup under Configuration|Options|Extensions|User Files. On measurement start they are copied to a special synchronization directory on the remote device. CAPL file functions called on a remote runtime kernel implicitly resolve a given file name to a file path based on this synchronization directory.

Files that are only used for write access may also be pre-defined as mentioned above. If they have not been pre-defined they will be implicitly registered as user files for the current measurement. All files created or changed on the remote device are transferred back to the user PC on end of measurement.

The CAPL functions that require a file name also accept a path preceding the file name. If the file name is already registered the path component is just ignored. In case of implicitly registered user files the file path is interpreted as the file path on the user PC to which the file is copied on measurement end.

CAPL functions setFilePath, setWritePath and getAbsFilePath are not available in case of a distributed environment.
