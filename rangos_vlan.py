def main():
    """
    Verificación del tipo de VLAN - normal / extendida
    """
    vlan_id = int(input("Favor introducir ID de VLAN : "))
    if 1 <= vlan_id <= 1005:
        print(f"Vlan ingresada {vlan_id} corresponde a rango normal.")
    elif 1006 <= vlan_id <= 4095:
        print(f"Vlan ingresada {vlan_id} corresponde a rango extendido.")
if __name__ == "__main__":
    main()        

