import { Injectable } from '@angular/core';
import { Producto } from '../models/producto.model';
import { PedidoDetalle } from '../models/PedidoDetalle.model';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

  private productos: Producto[] = [];
  private contadorId = 1;

  guardarProducto(producto: Producto) {
    producto.id = this.contadorId++;
    this.productos.push(producto);
  }

  mostrarProductos(): Producto[] {
    return this.productos;
  }

  eliminarProducto(id: number) {
    this.productos = this.productos.filter(p => p.id !== id);
  }

  actualizarProducto(productoActualizado: Producto) {
    const index = this.productos.findIndex(p => p.id === productoActualizado.id);

    if (index !== -1) {
      this.productos[index] = productoActualizado;
    }
  }

  // 🔥 VALIDAR STOCK
  tieneStock(productoId: number, cantidad: number): boolean {
    const producto = this.productos.find(p => p.id === productoId);
    return producto ? producto.stock >= cantidad : false;
  }

  // 🔥 DESCONTAR STOCK
  descontarStock(detalles: PedidoDetalle[]) {
    detalles.forEach(d => {
      const producto = this.productos.find(p => p.id === d.productoId);
      if (producto) {
        producto.stock -= d.cantidad;
      }
    });
  }

  // 🔥 RESTAURAR STOCK (EDITAR PEDIDO)
  restaurarStock(detalles: PedidoDetalle[]) {
    detalles.forEach(d => {
      const producto = this.productos.find(p => p.id === d.productoId);
      if (producto) {
        producto.stock += d.cantidad;
      }
    });
  }
}