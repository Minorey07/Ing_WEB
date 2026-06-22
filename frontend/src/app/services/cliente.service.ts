import { Injectable } from '@angular/core';
import { BaseHttpService } from './base-http.service';
import { Cliente } from '../models/cliente.model';

@Injectable({ providedIn: 'root' })
export class ClienteService {
  constructor(private http: BaseHttpService) {}

  listar(): Promise<Cliente[]> {
    return this.http.get<Cliente[]>('/clientes/');
  }

  crear(cliente: Cliente): Promise<Cliente> {
    return this.http.post<Cliente>('/clientes/', cliente);
  }

  actualizar(cliente: Cliente): Promise<Cliente> {
    return this.http.put<Cliente>(`/clientes/${cliente.id}`, cliente);
  }

  eliminar(id: number): Promise<void> {
    return this.http.delete<void>(`/clientes/${id}`);
  }
}
