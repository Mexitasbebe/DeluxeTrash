name = "potrace"

from .potrace import (
    Bitmap,
    Path,
    Curve,
    BezierSegment,
    CornerSegment,
    POTRACE_CORNER,
    POTRACE_CURVETO,
    POTRACE_TURNPOLICY_BLACK,
    POTRACE_TURNPOLICY_MAJORITY,
    POTRACE_TURNPOLICY_WHITE,
    POTRACE_TURNPOLICY_MINORITY,
    POTRACE_TURNPOLICY_RIGHT,
    POTRACE_TURNPOLICY_LEFT,
    POTRACE_TURNPOLICY_RANDOM,
)

# Se pueden agregar exportaciones de nuevas clases o constantes relacionadas con colores aquí.
# Por ejemplo, si has añadido una clase Color o constantes relacionadas con el manejo de colores.
# from .color import Color  # Ejemplo de cómo incluir una clase de color
