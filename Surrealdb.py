import subprocess
subprocess.run("surreal start --user root --pass root file:/home/miku/SurrealDatabases/localdb.db", shell=True)