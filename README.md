# El-pepe-85-markup-lang-
(Opcional)

Es un lenguaje de marcado de texto bien pitero.

Además, este lenguaje es la *revelación* más importante que he tenido en todo este tiempo. Es como, hacer que Textile, Zim wiki y el markdown de Pandoc decidieran copiarse en su
tesis de grado y los tres entregarían este markup como proyecto final xdddd.

## Características

Es un lenguaje con reglas **ESTRICTAS**, es decir, no entiende qué hacer si le pones una etiqueta de abrir bloque y luego no lo cierras. Si te atreves a tal cosa, no te olvides de
las consecuencias en el HTML final. XD. Así de malo es.
Retiene los bloques multilíneas heredados de los *fenced blocks* de Pandoc, pero extendiéndolos a incluir los párrafos como uno de estos (sí, de manera estricta).

Posee dos reglas diferentes para los encabezados, porque supuse que así sería más intrigante y divertido:
- Encabezados de 6 niveles con los "=", los de markdown de toda la vida.
- Encabezados de 6 niveles estilo Zim wiki.

<!--
Si no sabe qué es Zim wiki, tarea para la casa.

Si sí, entonces se hace una idea de lo paradójico que es haberlos puesto juntos, y así quería que fuera.
-->

```zim
====== TÍTULO 1 ======
===== TÍTULO 2 =====
==== TÍTULO 3 ====
=== TÍTULO 4 ===
== TÍTULO 5 ==
= TÍTULO 6 =
```

El cuerpo del html se comienza hasta que la orden es dada, y dichos bloques se introducen al encerrar el cuerpo entre las etiquetas `::body` y `body::`

```pp85
::body

<!-- Write here your TEXT -->

body::
```

Como el cuerpo debe indicarse de esta manera, de hecho, significa que el encabezado del HTML no se ha definido aún (eso implica, que eres completamente libre de hacer exactamente
lo que más gustes sobre esto, es más, esa es toda la libertad de pepe-85, que no tienes que añadir archivos gigantes y extensiones innumerables para poder hacer un documento
funcional que de otra forma es con características nativas de HTML y de CSS).

Nótese que, puedes hacer el encabezado como exactamente gustes (como en HTML XD), lo que significa, construir el estilo a mano, o por lo contrario importar archivos CSS como un
stylesheet. Por su parte, es totalmente sencillo escribir el encabezado como, un encabezado de tu propio archivo de texto antes de iniciar la instrucción `::body`. Detrás de esa
instrucción, todo se comporta como HTML puro.

```pp85

<head>

  <style>
    /*
    */
  </style>

</head>

::body

<!-- Write here your TEXT -->

body::
```

Las demás características se me están olvidando, las anotaré luego.




