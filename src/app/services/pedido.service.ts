import { Injectable } from '@angular/core';
import { Pedido } from '../models/pedido.model';

@Injectable({
  providedIn: 'root'
})
export class PedidoService {

  private pedidos: Pedido[] = [];
  private contadorId = 1;

  guardarPedido(pedido: Pedido) {
    pedido.id = this.contadorId++;

    this.pedidos.push({
      ...pedido,
      detalles: [...pedido.detalles]
    });
  }

  mostrarPedidos(): Pedido[] {
    return [...this.pedidos];
  }

  eliminarPedido(id: number) {
    this.pedidos = this.pedidos.filter(p => p.id !== id);
  }

  actualizarPedido(pedidoActualizado: Pedido) {
    const index = this.pedidos.findIndex(p => p.id === pedidoActualizado.id);

    if (index !== -1) {
      this.pedidos[index] = {
        ...pedidoActualizado,
        detalles: [...pedidoActualizado.detalles]
      };
    }
  }
}