import { Injectable } from '@angular/core';
import { Proveedor } from '../models/proveedor.model';

@Injectable({
  providedIn: 'root'
})
export class ProveedorService {

  private proveedores: Proveedor[] = [];

  private contadorId = 1;

  guardarProveedor(proveedor: Proveedor) {

    proveedor.id = this.contadorId++;

    this.proveedores.push(proveedor);

  }

  mostrarProveedores(): Proveedor[] {

    return this.proveedores;

  }

  eliminarProveedor(id: number) {

    this.proveedores =
      this.proveedores.filter(
        proveedor => proveedor.id !== id
      );

  }

  actualizarProveedor(proveedorActualizado: Proveedor) {

    const indice =
      this.proveedores.findIndex(
        proveedor => proveedor.id === proveedorActualizado.id
      );

    if (indice !== -1) {

      this.proveedores[indice] =
        proveedorActualizado;

    }

  }

}