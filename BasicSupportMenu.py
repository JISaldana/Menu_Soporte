import os

def ejecutar_scandisk():
    print("Ejecutando ScanDisk en la unidad C...")
    os.system("chkdsk C: /f")
    input("Presiona Enter para continuar...")

def listar_actualizaciones():
    print("Mostrando la lista de actualizaciones recientes...")
    os.system("wmic qfe list brief /format:table")
    input("Presiona Enter para continuar...")

def verificar_conectividad():
    print("Verificando conectividad a Internet (Ping a 8.8.8.8)...")
    os.system("ping 8.8.8.8")
    input("Presiona Enter para continuar...")

def mostrar_config_red():
    print("Mostrando configuración completa de red...")
    os.system("ipconfig /all")
    input("Presiona Enter para continuar...")

def limpiar_cache_dns():
    print("Limpiando caché de DNS...")
    os.system("ipconfig /flushdns")
    input("Presiona Enter para continuar...")

def reparar_imagen_dism():
    print("Reparando imagen del sistema con DISM...")
    os.system("dism /online /cleanup-image /restorehealth")
    input("Presiona Enter para continuar...")

def verificar_integridad_sfc():
    print("Verificando y reparando archivos del sistema...")
    os.system("sfc /scannow")
    input("Presiona Enter para continuar...")

def listar_procesos_activos():
    print("Listando procesos activos...")
    os.system("tasklist")
    input("Presiona Enter para continuar...")

def liberar_espacio_disco():
    print("Ejecutando limpieza de disco...")
    os.system("cleanmgr")
    input("Presiona Enter para continuar...")

def listar_servicios_activos():
    print("Listando servicios en ejecución...")
    os.system("net start")
    input("Presiona Enter para continuar...")

def reiniciar_red():
    print("Reiniciando configuración de red...")
    os.system("netsh int ip reset")
    os.system("netsh winsock reset")
    input("Presiona Enter para continuar...")

def comprobar_estado_fsutil():
    print("Comprobando el estado del sistema de archivos...")
    os.system("fsutil dirty query C:")
    input("Presiona Enter para continuar...")

def mostrar_uso_disco():
    print("Mostrando el uso del espacio en disco...")
    os.system("wmic logicaldisk get size,freespace,caption")
    input("Presiona Enter para continuar...")

def mostrar_rendimiento():
    print("Mostrando estadísticas de rendimiento del sistema...")
    os.system("wmic cpu get loadpercentage")
    os.system("wmic memorychip get capacity,devicelocator,partion")
    input("Presiona Enter para continuar...")

def verificar_proxy():
    print("Verificando la configuración del proxy...")
    os.system("netsh winhttp show proxy")
    input("Presiona Enter para continuar...")

def verificar_servicio_update():
    print("Verificando el estado del servicio de Windows Update...")
    os.system("sc query wuauserv")
    input("Presiona Enter para continuar...")

def analizar_uso_red():
    print("Analizando el uso de la red...")
    os.system("netstat -e")
    input("Presiona Enter para continuar...")

def mostrar_eventos_error():
    print("Mostrando los eventos de error recientes...")
    os.system("eventvwr.msc")
    input("Presiona Enter para continuar...")

def deshabilitar_servicio():
    print("Deshabilitando un servicio...")
    servicio = input("Ingresa el nombre del servicio que quieres deshabilitar: ")
    os.system(f"sc config {servicio} start= disabled")
    input(f"El servicio {servicio} ha sido deshabilitado. Presiona Enter para continuar...")

def generar_informe_sistema():
    print("Generando un informe completo del sistema...")
    os.system("systeminfo > informe_sistema.txt")
    print("Informe guardado como informe_sistema.txt")
    input("Presiona Enter para continuar...")

def ejecutar_solucionador():
    print("Ejecutando el solucionador de problemas de red...")
    os.system("msdt.exe /id NetworkDiagnosticsNetworkAdapter")
    input("Presiona Enter para continuar...")


def mostrar_menu():
    while True:
        print("\n===== Herramientas de Soporte Técnico =====")

        # Menú de diagnóstico de red
        print("\n[Diagnóstico de Red]")
        print("[1] Verificar conectividad a Internet")
        print("[2] Mostrar configuración de red completa")
        print("[3] Limpiar caché de DNS")
        print("[4] Reiniciar configuración de red")
        print("[5] Verificar configuración del proxy de red")
        print("[6] Analizar el uso de la red")

        # Menú de mantenimiento del sistema
        print("\n[Mantenimiento del Sistema]")
        print("[7] Ejecutar ScanDisk (CHKDSK)")
        print("[8] Desplegar lista de actualizaciones recientes de Windows")
        print("[9] Reparar imagen del sistema (DISM)")
        print("[10] Verificar integridad de archivos del sistema (SFC)")
        print("[11] Ejecutar limpieza de disco")
        print("[12] Generar informe del sistema")

        # Menú de servicios y procesos
        print("\n[Servicios y Procesos]")
        print("[13] Listar procesos activos")
        print("[14] Listar servicios en ejecución")
        print("[15] Verificar el estado del servicio de Windows Update")
        print("[16] Deshabilitar servicios innecesarios")

        # Menú de diagnóstico avanzado
        print("\n[Diagnóstico Avanzado]")
        print("[17] Comprobar estado del sistema de archivos (fsutil)")
        print("[18] Mostrar uso del espacio en disco")
        print("[19] Mostrar estadísticas de rendimiento del sistema")
        print("[20] Mostrar eventos de error recientes")

        print("\n[0] Salir")

        opcion = input("Selecciona una opción: ")

        # Llamada a las funciones según la selección
        if opcion == "1":
            verificar_conectividad()
        elif opcion == "2":
            mostrar_config_red()
        elif opcion == "3":
            limpiar_cache_dns()
        elif opcion == "4":
            reiniciar_red()
        elif opcion == "5":
            verificar_proxy()
        elif opcion == "6":
            analizar_uso_red()
        elif opcion == "7":
            ejecutar_scandisk()
        elif opcion == "8":
            listar_actualizaciones()
        elif opcion == "9":
            reparar_imagen_dism()
        elif opcion == "10":
            verificar_integridad_sfc()
        elif opcion == "11":
            liberar_espacio_disco()
        elif opcion == "12":
            generar_informe_sistema()
        elif opcion == "13":
            listar_procesos_activos()
        elif opcion == "14":
            listar_servicios_activos()
        elif opcion == "15":
            verificar_servicio_update()
        elif opcion == "16":
            deshabilitar_servicio()
        elif opcion == "17":
            comprobar_estado_fsutil()
        elif opcion == "18":
            mostrar_uso_disco()
        elif opcion == "19":
            mostrar_rendimiento()
        elif opcion == "20":
            mostrar_eventos_error()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()