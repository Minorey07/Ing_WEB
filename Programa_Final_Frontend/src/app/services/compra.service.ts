import { Injectable } from '@angular/core';
import { BaseHttpService } from './base-http.service';
import { Compra } from '../models/compra.model';

@Injectable({ providedIn: 'root' })
export class CompraService {
  constructor(private http: BaseHttpService) {}

  listar(): Promise<Compra[]> {
    return this.http.get<Compra[]>('/compras/');
  }

  crear(compra: Compra): Promise<Compra> {
    return this.http.post<Compra>('/compras/', compra);
  }

  actualizar(compra: Compra): Promise<Compra> {
    return this.http.put<Compra>(`/compras/${compra.id}`, compra);
  }

  eliminar(id: number): Promise<void> {
    return this.http.delete<void>(`/compras/${id}`);
  }
}
