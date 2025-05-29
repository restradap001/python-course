
# python-course

Repositorio de curso de Python con lecciones estructuradas, ejercicios prácticos y proyectos reales para dominar Python desde nivel principiante hasta avanzado.

## Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (para usar Dev Containers)
- Extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) en VS Code

### Instalación de los prerrequisitos

**Visual Studio Code:**
Sigue las instrucciones en https://code.visualstudio.com/download

**Git:**
Sigue las instrucciones en https://git-scm.com/downloads

**Docker Desktop:**
Descarga e instala desde https://www.docker.com/products/docker-desktop/

**Extensión Dev Containers:**
1. Abre VS Code
2. Ve a la sección de extensiones (Ctrl+Shift+X)
3. Busca "Dev Containers" e instálala


## Instalación y uso con Dev Containers

1. **Abrir en VS Code con Dev Containers**
   - Instala la extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) en VS Code.
   - Abre la carpeta del proyecto en VS Code.
   - Haz clic en la esquina inferior izquierda y selecciona “Reabrir en contenedor” (Reopen in Container).
   - Espera a que se construya y abra el entorno de desarrollo.

## Crear y activar un ambiente virtual de Python

Aunque el Dev Container ya incluye Python, puedes crear un ambiente virtual para aislar tus dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # Si es necesario
```

## Ejecutar archivos `.py` usando Run and Debug de VS Code

1. Abre el archivo `.py` que deseas ejecutar.
2. Haz clic en el botón **Run and Debug** (▶️) en la parte superior derecha del editor, o presiona `F5`.
3. Selecciona el entorno de Python adecuado si es la primera vez.
4. El resultado aparecerá en la terminal integrada o en la consola de depuración.
