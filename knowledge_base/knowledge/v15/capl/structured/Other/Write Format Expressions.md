# Write Format Expressions

> Category: `Other` | Type: `notes`

## Description

List of legal format expressions and differences between Windows and Linux:

Display Description

Format Windows

Format Linux

| CAPL Type | Display Description | Format Windows | Format Linux |
|---|---|---|---|
| int | signed display | %d | %d |
| long | signed display | %ld | %d |
| int64 | signed display | %I64d or %lld | %ld or %lld |
| byte/word | unsigned display | %u | %u |
| dword | unsigned display | %lu | %u |
| qword | unsigned display | %I64u or %llu | %lu or %llu |
| byte/word/int | hexadecimal display | %x | %x |
| dword/long | hexadecimal display | %lx | %x |
| qword/int64 | hexadecimal display | %I64x or %llx | %lx or %llx |
| byte/word/int | hexadecimal display (upper case) | %X | %X |
| dword/long | hexadecimal display (upper case) | %lX | %X |
| qword/int64 | hexadecimal display (upper case) | %I64X or %llX | %lX or %llX |
| byte/word/int | octal display | %o | %o |
| dword/long | octal display | %lo | %o |
| qword/int64 | octal display | %I64o or %llo | %lo or %llo |
| float/double | floating point display | %g or %f | %g or %f |
| character display | %c | %c |  |
| string display | %s | %s |  |
| display of %-character | %% | %% |  |
| dword | 32-bit pointer (without implicit pointer format 0xABABABAB) | %p | %08x |
| 32-bit pointer (with implicit pointer format 0xABABABAB) | %#p | %p |  |
| qword | 64-bit pointer (without implicit pointer format 0xABABABABABABABAB) | %I64p | %016lx |
| 64-bit pointer (with implicit pointer format 0xABABABABABABABAB) | %#I64p | %p |  |

| Note The %n format is invalid and must not be used. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
