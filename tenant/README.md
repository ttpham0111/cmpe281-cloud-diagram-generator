## Tenant 1
Command:
```
java -jar /app/app/resources/ProjectUml.jar {} pic
```

Mode: file
Output Extension: `.jpeg`

## Tenant 2
Command:
```
java -Dzanthan.prefs=/app/app/resources/diagram.preferences -jar /app/app/resources/sequence.jar --headless {}
```

Mode: code
Output Extension: `.png`

## Tenant 3
Command:
```
/app/app/resources/umlgraph {} png
```

Mode: code
Input Extension: `.java`
Output Extension: `.png`

## Tenant 4
Command:
```
/app/app/resources/umple {}
```

Mode: code
Output Extension: `.png`