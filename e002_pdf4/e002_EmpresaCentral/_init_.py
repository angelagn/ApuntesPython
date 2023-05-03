#Importar 1 modulo del paquete compras
import Compras.CompraClientes
#Importar una variable con alias
from Contabilidad.PagoTransporte import pagoT1 as Conta
# importar el paquete Facturaciòn
import Facturacion.CajaMenor
import Facturacion.FacturasCompras
import Facturacion.FacturasVentas

#Importar el paquete de I+D
import InvestigacionYDesarrollo.Divulgacion

#Importar paquete ventas
import Ventas.VentaDeEquipos
import Ventas.VentaRepuestos
import Ventas.VentaServicios



#Imprimir sus variables
print("**************************************************************************")
print("--Variables en modulo compra clientes:\n ", Compras.CompraClientes.compra1)
print(Compras.CompraClientes.compra2)
print(Compras.CompraClientes.compra3)



#Imprimir variables del paquete contabilidad
print("**************************************************************************")
print("--Variable pagoT1 del modulo PagoTransporte: ", Conta) #Imprime 200

#Imprimir todos los modulos del paquete facturaciòn
print("**************************************************************************")
print("--Modulos del paquete facturaciòn")
Facturacion.CajaMenor.cajaM() # Imprime 50
Facturacion.FacturasCompras.FCompras() #Imprime string- 
Facturacion.FacturasVentas.TVentas()

#Importar la variable
from Facturacion.FacturasVentas import totalventas
print(totalventas) # imprime 500

#Importar de I+D
print("**************************************************************************")
print("--I+D")
InvestigacionYDesarrollo.Divulgacion.Formacion()

#Imprimir variables modulo ventas
print("**************************************************************************")
print("--Ventas")

print(Ventas.VentaDeEquipos.servicios)
print(Ventas.VentaDeEquipos.servicios1)
print(Ventas.VentaDeEquipos.servicios2)

#Imprimir variables del mòdulo ventas de repuestos
print("**************************************************************************")
print("--Servicios de repuestos")
print(Ventas.VentaRepuestos.val1)
print(Ventas.VentaRepuestos.val2)
print(Ventas.VentaRepuestos.val3)

#llamar funciòn del modulo venta de servicios
print("**************************************************************************")
print("--Venta servicios")
Ventas.VentaServicios.VentaServicios()