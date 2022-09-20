from cuenta_bancaria import CuentaBancaria 
cuenta1 = CuentaBancaria(0.15, 100)
cuenta1.deposito(300).mostrar_info_cuenta()
cuenta1.generar_interes().mostrar_info_cuenta()

cuenta2 = CuentaBancaria(0.15, 50)

print(CuentaBancaria.todas_las_cuentas)