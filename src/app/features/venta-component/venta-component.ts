import { Component, inject } from '@angular/core';

import { PedidoService } from '../../services/pedido.service';
import { Pedido } from '../../models/pedido.model';

@Component({
  selector: 'app-venta-component',
  imports: [],
  templateUrl: './venta-component.html',
  styleUrl: './venta-component.css',
})
export class VentaComponent {

  pedidoService = inject(PedidoService);

  listaVentas: Pedido[] = [];

  constructor() {

    this.mostrarVentas();

  }

  mostrarVentas() {

    this.listaVentas =
      this.pedidoService
        .mostrarPedidos()
        .filter(
          pedido =>
            pedido.estado === 'ENTREGADO'
        );

  }

  get totalVentas(): number {

    return this.listaVentas.reduce(
      (total, venta) =>
        total + venta.total,
      0
    );

  }

}