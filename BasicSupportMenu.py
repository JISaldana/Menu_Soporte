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
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
