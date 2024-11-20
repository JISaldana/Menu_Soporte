# Soporte Técnico CMD - Herramientas en Python

Este es un script en Python que recopila y ejecuta comandos útiles de la terminal de Windows (CMD) para diagnosticar y resolver problemas comunes de sistemas. El script presenta un menú interactivo donde el usuario puede seleccionar distintas opciones para ejecutar herramientas como el análisis de disco, ver actualizaciones recientes, limpiar caché de DNS y más.

## Comandos Disponibles

El script ofrece las siguientes opciones:

1. **Ejecutar ScanDisk (CHKDSK)**  
2. **Desplegar lista de actualizaciones recientes de Windows** 
3. **Verificar conectividad a Internet**  
4. **Mostrar configuración de red completa**  
5. **Limpiar caché de DNS**  
6. **Reparar imagen del sistema (DISM)**  
7. **Verificar integridad de archivos del sistema (SFC)**  
8. **Listar procesos activos**  
9. **Ejecutar limpieza de disco**  
10. **Listar servicios en ejecución**  
11. **Reiniciar configuración de red**
12. **Comprobar el estado del sistema de archivos (fsutil)
13. **Mostrar uso del espacio en disco
14. **Mostrar estadísticas de rendimiento del sistema
15. **Verificar configuración del proxy de red
16. **Verificar el estado del servicio de Windows Update
17. **Analizar el uso de la red
18. **Mostrar eventos de error recientes
19. **Deshabilitar servicios innecesarios
20. **Generar informe del sistema
21. **Ejecutar solucionador de problemas de red


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
