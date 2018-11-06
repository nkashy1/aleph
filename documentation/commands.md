# ...

Django for machine learning.

Define an interface that data must already come in the format as, e.g. our csv + tar files

There is a build command to generate the project, start training on a particular model

Need a way to pass hyperparameters into models

## Commands

Aleph commands update a toml (json) config file that is parsed at build time to generate other python files (and jupyter notebooks?)

```
aleph init
```

```
aleph activate
```

```
aleph dataset list
```

```
aleph dataset add <name> <location> --training | --eval | --test
```

```
aleph dataset remove <name>
```

```
aleph features list
```

```
aleph features add <name> <type> <shape>
```

```
aleph features remove <name>
```

```
aleph labels list
```

```
aleph labels add <name> <type> <shape>
```

```
aleph labels remove <name>
```

```
aleph optimizers list
```

```
aleph optimizers add <name> <type> <parameter1>=<value1> ... <parameterN>=<valueN>
```

```
aleph optimizers get <name>
```

```
aleph optimizers update <name> <type> <parameter1>=<value1> ... <parameterN>=<valueN>
```

```
aleph optimizers remove <name>
```

```
aleph models add <name> <modelspec>
```

```
aleph models list
```

```
aleph models delete <name>
```

```
aleph build    # builds tfrecords files, error checking/validation -> generate aleph.py
```

```
aleph train    # Kick off training, will probably take some command line flags
```

```
aleph export
```

```
aleph serve
```

## init

https://github.com/phildow/ml-template

(Cross-check against https://github.com/GoogleCloudPlatform/cloudml-samples/tree/master/cloudml-template)

Generating project files, templating out notebooks, create and activate virtual environment, install modules

```
/project
 aleph.py	#  created by aleph build
 /models
   tfhub-name.py
 /optimizers
 /input_functions
 /
 /losses
 /dataset
  __init__.py
  a.py
  b.py
```

```

```