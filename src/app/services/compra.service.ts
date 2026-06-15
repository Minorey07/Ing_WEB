import { Injectable } from '@angular/core';
import { Compra } from '../models/compra.model';

@Injectable({
  providedIn: 'root'
})
export class CompraService {

  private compras: Compra[] = [];

  private contadorId = 1;

  guardarCompra(compra: Compra) {

    compra.id = this.contadorId++;

    this.compras.push(compra);

  }

  mostrarCompras(): Compra[] {

    return this.compras;

  }

  eliminarCompra(id: number) {

    this.compras =
      this.compras.filter(
        compra => compra.id !== id
      );

  }

  actualizarCompra(compraActualizada: Compra) {

    const indice =
      this.compras.findIndex(
        compra => compra.id === compraActualizada.id
      );

    if (indice !== -1) {

      this.compras[indice] =
        compraActualizada;

    }

  }

}