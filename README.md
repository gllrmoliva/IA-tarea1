## Como ejecutar
Ejecuta el script principal desde la terminal utilizando los siguientes argumentos:

* `--agent`: tipo de agente (`player`, `random`, `bfs`, `dfs`). Por defecto: `random`.
* `--input`: ruta al archivo .txt que contiene los mapas.
* `--gui`: activa la interfaz gráfica al añadirlo.

Ejemplos ejecución:

* Modo player: 
```bash 
python -m main --agent player --input input.txt
```

* BFS con gui:
```bash
python -m main --agent bfs --input input.txt --gui
```

* DFS sin gui:
```bash
python -m main --agent bfs --input input.txt
```

> Al utilizar gui para avanzar con agentes automáticos, presionar tecla SPACE para realizar el siguiente movimiento.

> Agente player se mueve con las flechas.
