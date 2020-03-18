# CBDV Programming Challenge
Given a JSON file that encodes a nested key-value strucuture, write a program
that stores each key in the structure, and how many times it occurred. This
newly created mapping should be converted to JSON, then printed to STDOUT.

To reduce the number of potential edge cases, you can assume the following
limitations on the JSON. All keys are strings. All values are either objects,
arrays, or strings. If an array is present, each element may be an object,
string, or other array.

Here is a small inline example. More example files are provided in the examples
folder, along with their respective solutions.

```json
{
  "omu": "ate",
  "lusb": [
    {
      "omu": [
        "ata",
        "osi"
      ]
    },
    {
      "lusb": "lul"
    },
    {
      "mas": "ote"
    },
    {
      "ebi": "ilo"
    }
  ]
}
```

```json
{
  "ebi": 1,
  "lusb": 2,
  "mas": 1,
  "omu": 2,
}
```
