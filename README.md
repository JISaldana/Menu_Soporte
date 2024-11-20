# Soporte Técnico CMD - Herramientas en Python

Este es un script en Python que recopila y ejecuta comandos útiles de la terminal de Windows (CMD) para diagnosticar y resolver problemas comunes de sistemas. El script presenta un menú interactivo donde el usuario puede seleccionar distintas opciones para ejecutar herramientas como el análisis de disco, ver actualizaciones recientes, limpiar caché de DNS y más.

## Comandos Disponibles

El script ofrece las siguientes opciones:

1. **Ejecutar ScanDisk (CHKDSK)**  
   Realiza un chequeo del disco y corrige errores en la unidad C:.

2. **Desplegar lista de actualizaciones recientes de Windows**  
   Muestra las actualizaciones recientes que se han instalado en el sistema.

3. **Verificar conectividad a Internet**  
   Realiza un *ping* a 8.8.8.8 para verificar la conectividad con la red.

4. **Mostrar configuración de red completa**  
   Muestra la configuración completa de la red del sistema, incluyendo direcciones IP y detalles de la red.

5. **Limpiar caché de DNS**  
   Limpia la caché DNS para solucionar problemas de resolución de nombres de dominio.

6. **Reparar imagen del sistema (DISM)**  
   Repara los archivos del sistema de Windows utilizando la herramienta DISM (Deployment Imaging Service and Management Tool).

7. **Verificar integridad de archivos del sistema (SFC)**  
   Verifica y repara archivos del sistema dañados utilizando la herramienta SFC (System File Checker).

8. **Listar procesos activos**  
   Muestra todos los procesos en ejecución en el sistema.

9. **Ejecutar limpieza de disco**  
   Ejecuta el limpiador de disco para liberar espacio en el sistema.

10. **Listar servicios en ejecución**  
    Muestra todos los servicios que se están ejecutando en el sistema.

11. **Reiniciar configuración de red**  
    Restaura la configuración de la red y el socket Winsock.

## Requisitos

- Python 3.x instalado en tu sistema.
- Acceso de administrador (algunos comandos requieren privilegios elevados).

## Instrucciones de Uso

1. **Descargar el script**  
   Descarga el archivo `.py` o clona el repositorio.

2. **Ejecutar el script**  
   Abre la terminal o línea de comandos, navega hasta el directorio donde guardaste el archivo y ejecuta el siguiente comando:

   ```bash
   python nombre_del_script.py
   ```

3. **Seleccionar una opción**  
   El programa te mostrará un menú interactivo. Selecciona el número correspondiente al comando que deseas ejecutar.

4. **Resultados**  
   El programa ejecutará el comando y mostrará los resultados en la terminal. Luego, podrás elegir otra opción o salir.

## Ejemplo de Uso

Al ejecutar el script, verás algo como esto:

```
===== Herramientas de Soporte Técnico =====
[1] Ejecutar ScanDisk (CHKDSK)
[2] Desplegar lista de actualizaciones recientes de Windows
[3] Verificar conectividad a Internet
[4] Mostrar configuración de red completa
[5] Limpiar caché de DNS
[6] Reparar imagen del sistema (DISM)
[7] Verificar integridad de archivos del sistema (SFC)
[8] Listar procesos activos
[9] Ejecutar limpieza de disco
[10] Listar servicios en ejecución
[11] Reiniciar configuración de red
[0] Salir
Selecciona una opción:
```

Después de seleccionar la opción, por ejemplo, [1], el programa ejecutará `chkdsk C: /f` y te pedirá que presiones Enter para continuar.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un *fork* del repositorio, hacer mejoras o agregar nuevos comandos útiles. Cualquier sugerencia es bienvenida.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
