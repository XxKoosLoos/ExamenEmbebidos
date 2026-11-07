# Registro de cambios

## 2026-11-07 (UTC)

### Documentación del estado real

- **Motivo:** facilitar la evaluación profesional del repositorio con información respaldada por la auditoría.
- **Alcance:** actualización de `README.md` en [`08e44be`](https://github.com/XxKoosLoos/ExamenEmbebidos/commit/08e44be586e33429318f125df88656f21fb035fd) y creación de este `CHANGELOG.md`.
- **Contenido:** descripción del prototipo, dependencias observadas, instrucciones propuestas, limitaciones técnicas y atribución conservada de los seis integrantes.
- **Validación:** revisión documental. No se ejecutaron aplicaciones ni se realizaron pruebas de hardware.
- **Historial:** se conservan los commits y ramas originales, sin reescritura del historial.
- **Límites:** no se modificaron fuentes ni dependencias ni se añadieron funcionalidades.

### Exclusiones de archivos locales — 2026-11-07 (UTC)

- **Motivo:** evitar incorporar nuevos entornos virtuales, cachés, configuraciones locales potencialmente sensibles y metadatos de editores.
- **Alcance:** incorporación de `.gitignore` en [`3a77bd8`](https://github.com/XxKoosLoos/ExamenEmbebidos/commit/3a77bd8e1821ce0519f2a97ce75320ef8029c98b) y actualización de este registro.
- **Validación:** el parche se comprobó en un repositorio temporal independiente: 11 rutas excluidas y cuatro rutas permitidas, incluidas fuentes y `.env.example`.
- **Límites:** los archivos ya versionados permanecen en Git; no se eliminaron entornos ni secretos históricos. No se modificaron código, dependencias ni historial original. Las plantillas `.env.example` requieren revisión de contenido antes de publicarse.
