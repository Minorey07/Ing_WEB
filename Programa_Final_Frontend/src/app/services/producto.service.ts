import { Injectable } from '@angular/core';
import { BaseHttpService } from './base-http.service';
import { Producto } from '../models/producto.model';

@Injectable({ providedIn: 'root' })
export class ProductoService {
  constructor(private http: BaseHttpService) {}

  listar(): Promise<Producto[]> {
    return this.http.get<Producto[]>('/productos/');
  }

  crear(producto: Producto): Promise<Producto> {
    return this.http.post<Producto>('/productos/', producto);
  }

  actualizar(producto: Producto): Promise<Producto> {
    return this.http.put<Producto>(`/productos/${producto.id}`, producto);
  }

  eliminar(id: number): Promise<void> {
    return this.http.delete<void>(`/productos/${id}`);
  }
}
