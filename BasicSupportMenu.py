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
        print("[1] Ejecutar ScanDisk (CHKDSK)")
        print("[2] Desplegar lista de actualizaciones recientes de Windows")
        print("[3] Verificar conectividad a Internet")
        print("[4] Mostrar configuración de red completa")
        print("[5] Limpiar caché de DNS")
        print("[6] Reparar imagen del sistema (DISM)")
        print("[7] Verificar integridad de archivos del sistema (SFC)")
        print("[8] Listar procesos activos")
        print("[9] Ejecutar limpieza de disco")
        print("[10] Listar servicios en ejecución")
        print("[11] Reiniciar configuración de red")
        print("[12] Comprobar estado del sistema de archivos (fsutil)")
        print("[13] Mostrar uso del espacio en disco")
        print("[14] Mostrar estadísticas de rendimiento del sistema")
        print("[15] Verificar configuración del proxy de red")
        print("[16] Verificar el estado del servicio de Windows Update")
        print("[17] Analizar el uso de la red")
        print("[18] Mostrar eventos de error recientes")
        print("[19] Deshabilitar servicios innecesarios")
        print("[20] Generar informe del sistema")
        print("[21] Ejecutar solucionador de problemas de red")
        print("[0] Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejecutar_scandisk()
        elif opcion == "2":
            listar_actualizaciones()
        elif opcion == "3":
            verificar_conectividad()
        elif opcion == "4":
            mostrar_config_red()
        elif opcion == "5":
            limpiar_cache_dns()
        elif opcion == "6":
            reparar_imagen_dism()
        elif opcion == "7":
            verificar_integridad_sfc()
        elif opcion == "8":
            listar_procesos_activos()
        elif opcion == "9":
            liberar_espacio_disco()
        elif opcion == "10":
            listar_servicios_activos()
        elif opcion == "11":
            reiniciar_red()
        elif opcion == "12":
            comprobar_estado_fsutil()
        elif opcion == "13":
            mostrar_uso_disco()
        elif opcion == "14":
            mostrar_rendimiento()
        elif opcion == "15":
            verificar_proxy()
        elif opcion == "16":
            verificar_servicio_update()
        elif opcion == "17":
            analizar_uso_red()
        elif opcion == "18":
            mostrar_eventos_error()
        elif opcion == "19":
            deshabilitar_servicio()
        elif opcion == "20":
            generar_informe_sistema()
        elif opcion == "21":
            ejecutar_solucionador()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
