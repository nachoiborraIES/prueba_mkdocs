# Introducción a MkDocs

**MkDocs** es un framework que permite crear sitios web de documentación muy fácilmente, usando lenguaje *Markdown*.

## Requisitos previos

Para poder utilizar *MkDocs* es necesario tener instalado Python previamente. Además, necesitamos instalar las siguientes librerías usando el comando `pip`, bien en la distribución general del sistema, o en un entorno virtual propio (*venv*):

* El propio framework *mkdocs*, que podemos instalar a través de `pip` con el comando `pip install mkdocs`
* Si queremos utilizar algún tema de diseño externo a MkDocs, como por ejemplo el que usaremos aquí (*material*), lo debemos instalar también. El comando en este caso es `pip install mkdocs-material`

## Comandos útiles

Para crear el esqueleto de un sitio *MkDocs* podemos usar el comando `mkdocs new` indicando un nombre de carpeta (se creará una carpeta con dicho nombre en la carpeta donde estemos):

```
mkdocs new mi_web
```

Se creará una estructura de carpetas y archivos que explicaremos más adelante. Pero antes explicamos otros comandos útiles que podemos lanzar durante nuestra edición del sitio:

* `mkdocs serve` - Lanza un servidor local para probar la web. Cualquier cambio que hagamos en los contenidos o el estilo relanzará el servidor automáticamente, aunque es posible que algunos cambios profundos produzcan un error y necesitemos parar y reiniciar el servidor manualmente.
* `mkdocs build` - Se genera el sitio HTML completo en la subcarpeta `site` (para publicarlo en un servidor local o externo).
* `mkdocs -h` - Muestra ayuda en el terminal sobre el uso del comando
* `mkdocs gh-deploy` - Despliega la web en el repositorio asociado de GitHub (este paso se deberá hacer previamente), en una rama alternativa llamada `gh-pages`.

## Estructura de carpetas

La estructura de carpetas y archivos que se crea con el comando `mkdocs new` es la siguiente:

* `mkdocs.yml`: fichero de configuración general del sitio, en formato YAML
* `docs/`: subcarpeta donde colocaremos todos nuestros documentos Markdown que formarán parte de la web
* `docs/index.md`: fichero inicial de prueba (página raíz del sitio), con un contenido por defecto

## Aspectos relevantes de la configuración

Veremos a continuación algunos parámetros relevantes que podemos incluir en el fichero de configuración `mkdocs.yml`, y que se pueden consultar en el fichero de configuración de este mismo repositorio:

* `site_name`: nombre del sitio (aparecerá en la barra superior de navegación)
* `site_url`: URL principal del servidor donde se publicará
* `use_directory_urls`: a *true* hace URLs amigables, y a *false* deja las URL como páginas HTML (una por cada documento Markdown).
* `nav`: define nuestro menú de navegación (en el caso del tema *material*, se ubica en la parte izquierda). Especificamos el título de cada apartado y la página *Markdown* que se mostrará.
* `theme`: configura el tema CSS que se utilizará. Internamente admite varias opciones; aquí citamos las más habituales:
    * `language`: idioma de la web (en nuestro caso, `es`)
    * `name`: nombre del tema (en nuestro ejemplo, *material*)
    * `palette`: permite elegir la paleta de colores del tema. Podemos optar por una combinación simple de colores `primary` (barra de navegación y color de enlaces) y `accent` (color de elementos interactuables), o bien definir *esquemas*. En concreto *Material* dispone de un tema oscuro llamado *slate* y un tema claro llamdo *default*, y podemos configurar aquí los colores y cómo cambiar de uno a otro desde la propia web. Más información [aquí](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/).
    * `font`: permite especificar fuente para el texto (propiedad `text`) y para el código fuente (propiedad `code`).
    * `logo`: permite establecer el logo que aparecerá en la barra de navegación superior
    * `features`: características adicionales a incluir en el tema. Algunos ejemplos son `header.autohide` (para ocultar la barra de navegación superior cuando hacemos scroll por la página), `navigation.top` (para mostrar un botón para volver al inicio cuando hacemos scroll hacia abajo), o `toc.follow` (para mostrar en la barra de navegación el título de la página actual cuando hacemos scroll hacia abajo).

Aquí vemos un ejemplo de fichero de configuración, el que se usa para esta misma web:

```yaml
site_name: Página de prueba con Material for MkDocs
site_url: https://nahoiborraies.github.io/prueba_mkdocs
use_directory_urls: false

# Menú de navegación (izquierda)
nav:
  - Introducción: index.md
  - Características importantes: 
    - Opciones con el código fuente: 01.md
    - Subir documentación a GH Pages: 02.md

# Tema CSS
theme:
  language: es
  name: "material"
  palette:
    # Aquí se configuran los temas claro y oscuro, respectivamente
    - scheme: default
      primary: "blue"
      accent: "yellow"
      toggle:
        icon: material/toggle-switch-off-outline
        name: Cambiar a modo noche
    - scheme: slate 
      primary: "blue"
      accent: "yellow"
      toggle:
        icon: material/toggle-switch
        name: Cambiar a modo día
  font:
    text: Roboto
    code: Roboto Mono
  logo: "images/logo.png"
  features:
    - header.autohide
    - navigation.top
    - navigation.tracking
    - navigation.footer
    - navigation.indexes
    - content.code.annotate
    - announce.dismiss
    - toc.follow
    - content.code.copy

# CSS adicional
extra_css:
  - css/extra.css

# Opciones adicionales de configuración
extra:
  consent:
    title: Consentimiento de cookies
    description: >-
      Este sitio web utiliza cookies para ofrecerte una mejor experiencia. 
      Al hacer clic en "Aceptar", aceptas el uso de cookies. 
      También puedes configurar tus preferencias de cookies si lo prefieres.

# Plugins adicionales
plugins:
  - search

# Extensiones de Markdown habilitadas
markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - meta
  - pymdownx.details  
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.caret
  - pymdownx.mark
  - pymdownx.tilde
  - pymdownx.keys
  # Uso correcto de listas (no embebidas en otros elementos)
  - sane_lists
  - toc:
      permalink: true
      toc_depth: 4
```

Para más información, visitar [mkdocs.org](https://www.mkdocs.org) :smile:
