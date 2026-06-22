import { Injectable } from '@angular/core';
import { BaseHttpService } from './base-http.service';
import { Pedido } from '../models/pedido.model';

@Injectable({ providedIn: 'root' })
export class PedidoService {
  constructor(private http: BaseHttpService) {}

  listar(): Promise<Pedido[]> {
    return this.http.get<Pedido[]>('/pedidos/');
  }

  crear(pedido: Pedido): Promise<Pedido> {
    return this.http.post<Pedido>('/pedidos/', pedido);
  }

  actualizar(pedido: Pedido): Promise<Pedido> {
    return this.http.put<Pedido>(`/pedidos/${pedido.id}`, pedido);
  }

  eliminar(id: number): Promise<void> {
    return this.http.delete<void>(`/pedidos/${id}`);
  }
}
