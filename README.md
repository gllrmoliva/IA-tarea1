## Como ejecutar
Para ejecutar el programa ejecutar:
```bash 
python -m main [Args]
```


El script principal posee los siguientes argumentos:

* `--agent`: tipo de agente (`player`, `random`, `bfs`, `dfs`). Por defecto: `random`.
* `--input`: ruta al archivo .txt que contiene los mapas. (obligatorio)
* `--gui`: activa la interfaz gráfica al añadirlo.
> La gui es activada siempre con los agentes player y random.

### Ejemplos:

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

## Formato de entrada
Para ingresar nuevos laberintos al sistema este debe seguir el siguiente formato:

- número de filas (m)
- número de columnas (n)
- Fila de celda de inicio
- Columna de celda de inicio
- Fila de celda destino
- Columna de celda destino
- Número en cada casilla.

### Ejemplo
```
5 5 0 0 1 3
3 4 1 3 1
3 3 3 0 2
3 1 2 2 3
4 2 3 3 3
4 1 4 3 2
```
> Se considera que los inputs se entregan con el formato correcto.
