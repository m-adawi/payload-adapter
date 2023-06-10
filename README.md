## Example:
input:
```json
{
  "student_name": "malek",
  "student_age": 24,
  "_metadata": {
    "whatever": "bla"
  }
}
```
template:
```yaml
output:
  student:
    name: "{{ load.student_name | capitalize }}"
    age: "{{ load.student_age }}"
```
output
```json
{
  "student": {
    "age": "24",
    "name": "Malek"
  }
}

```

