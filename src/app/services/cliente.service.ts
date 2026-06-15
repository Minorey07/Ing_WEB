import { Injectable } from '@angular/core';
import { Cliente } from '../models/cliente.model';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {

  private clientes: Cliente[] = [];

  private contadorId = 1;

  guardarCliente(cliente: Cliente) {

    cliente.id = this.contadorId++;

    this.clientes.push(cliente);

  }

  mostrarClientes(): Cliente[] {

    return this.clientes;

  }

  eliminarCliente(id: number) {

    this.clientes =
      this.clientes.filter(
        cliente => cliente.id !== id
      );

  }

  actualizarCliente(clienteActualizado: Cliente) {

    const indice =
      this.clientes.findIndex(
        cliente => cliente.id === clienteActualizado.id
      );

    if (indice !== -1) {

      this.clientes[indice] =
        clienteActualizado;

    }

  }

}